from typing import Optional, cast, List

from fhir.resources.R4B.fhirtypes import HumanNameType, String
from fhir.resources.R4B.humanname import HumanName
from nominally import parse_name

from helix_personmatching.fhir_manager.parse_name_result import ParseNameResult
from helix_personmatching.standardizers.human_name_standardizer_result import (
    HumanNameStandardizerResult,
)
from helix_personmatching.utils.list_utils import get_first_element_or_null


class HumanNameStandardizer:
    @staticmethod
    def standardize(
        *, names: list[HumanNameType] | None, verbose: bool = False
    ) -> list[HumanNameStandardizerResult] | None:
        """
        Standardize a list of human names

        :param names: List of HumanName objects to standardize
        :param verbose: Whether to print verbose output
        :return: List of HumanNameStandardizerResult objects
        """
        if not names:
            return None

        assert isinstance(names, list)

        return [
            n
            for n in [
                HumanNameStandardizer.standardize_single(
                    name=name,
                    verbose=verbose,
                )
                for name in names
            ]
            if n is not None
        ]

    @staticmethod
    def standardize_single(
        *, name: HumanNameType | None, verbose: bool = False
    ) -> HumanNameStandardizerResult | None:
        """
        Standardize a single human name

        :param name: HumanName object to standardize
        :param verbose: Whether to print verbose output
        :return: HumanNameStandardizerResult object
        """
        if not name:
            return None

        assert isinstance(name, HumanName)

        first_name: Optional[str] = (
            name.given[0] if name and name.given and len(name.given) > 0 else None
        )
        family_name: Optional[str] = name.family if name else None
        middle_name: Optional[str] = (
            name.given[1] if name and name.given and len(name.given) > 1 else None
        )

        # try to parse names using nominally since the names can be stored in wrong fields
        parsed_name: Optional[ParseNameResult] = HumanNameStandardizer.safe_name_parse(
            name=name,
            verbose=verbose,
        )
        if parsed_name is not None:
            if parsed_name.first:
                first_name = parsed_name.first
            if parsed_name.middle:
                middle_name = parsed_name.middle
            if parsed_name.last:
                family_name = parsed_name.last

        standardized_name: HumanName = name.copy()
        if first_name:
            standardized_name.given = [cast(String, first_name)]
        if middle_name:
            standardized_name.given.append(cast(String, middle_name))
        if family_name:
            standardized_name.family = cast(String, family_name)

        return HumanNameStandardizerResult(
            name=cast(HumanNameType, standardized_name),
            middle_initial=middle_name[0]
            if middle_name and len(middle_name) > 0
            else None,
        )

    @staticmethod
    def safe_name_parse(
        *,
        name: Optional[HumanName],
        verbose: bool = False,
    ) -> Optional[ParseNameResult]:
        # noinspection PyUnresolvedReferences
        if name is None:
            return None

        assert isinstance(name, HumanName)

        if verbose:
            print("FhirToAttributeDict:safe_name_parse()...")

        combined_name = ""
        try:
            # if both family and given are populated then ignore text
            if name.given is not None and len(name.given) > 0 and name.family:
                combined_name += " ".join([str(g) for g in name.given])
                combined_name += f" {name.family}"
            elif name.text is not None:
                combined_name = name.text

            if not combined_name:
                return None
            result = parse_name(combined_name)
            return ParseNameResult(
                first=result.get("first"),
                middle=result.get("middle"),
                last=result.get("last"),
            )
        except Exception as e:
            if verbose:
                print(f"Exception (returning None): Parsing Name: {combined_name}: {e}")

            return None

    @staticmethod
    def get_primary_human_name(
        *, name: Optional[List[HumanNameType]]
    ) -> Optional[HumanNameType]:
        """
        Get the primary human name from a list of human names

        :param name: List of HumanName objects
        :return: HumanName object
        """
        if name is None:
            return None

        # The order of preference is:
        # https://hl7.org/FHIR/valueset-name-use.html
        # 1. usual
        # 2. official
        # 3. maiden
        # 4. others
        usual_name: Optional[HumanName] = get_first_element_or_null(
            [name1 for name1 in name if cast(HumanName, name1).use == "usual"]
        )
        if usual_name:
            return cast(HumanNameType, usual_name)

        official_name: Optional[HumanName] = get_first_element_or_null(
            [name1 for name1 in name if cast(HumanName, name1).use == "official"]
        )
        if official_name:
            return cast(HumanNameType, official_name)

        maiden_name: Optional[HumanName] = get_first_element_or_null(
            [name1 for name1 in name if cast(HumanName, name1).use == "maiden"]
        )
        if maiden_name:
            return cast(HumanNameType, maiden_name)

        return cast(Optional[HumanNameType], get_first_element_or_null(name))
