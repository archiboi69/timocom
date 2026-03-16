from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostalCodeAreas")


@_attrs_define
class PostalCodeAreas:
    """Multiple postal code areas of a country. Postal code area is determined by a postal code fragment (prefix).

    Attributes:
        country (str | Unset): 2 letter language code as defined by ISO 3166-1 alpha-2.
            A maximum of 5 different countries for start are
            supported. The same goes for destination.
            Currently supported values:
            * AD
            * AE
            * AF
            * AL
            * AM
            * AT
            * AZ
            * BA
            * BE
            * BG
            * BH
            * BY
            * CH
            * CN
            * CY
            * CZ
            * DE
            * DK
            * DZ
            * EE
            * EG
            * ER
            * ES
            * ET
            * FI
            * FO
            * FR
            * GB
            * GE
            * GI
            * GR
            * HR
            * HU
            * IE
            * IL
            * IN
            * IQ
            * IR
            * IS
            * IT
            * JO
            * KG
            * KW
            * KZ
            * LB
            * LI
            * LT
            * LU
            * LV
            * LY
            * MA
            * MC
            * MD
            * ME
            * MK
            * MN
            * MT
            * NL
            * NO
            * NP
            * OM
            * PK
            * PL
            * PT
            * QA
            * RO
            * RS
            * RU
            * SA
            * SE
            * SI
            * SK
            * SM
            * SY
            * TJ
            * TM
            * TN
            * TR
            * UA
            * UZ
            * VA
            * YE Example: ES.
        postal_codes (list[str] | Unset):
    """

    country: str | Unset = UNSET
    postal_codes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        postal_codes: list[str] | Unset = UNSET
        if not isinstance(self.postal_codes, Unset):
            postal_codes = self.postal_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if postal_codes is not UNSET:
            field_dict["postalCodes"] = postal_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country", UNSET)

        postal_codes = cast(list[str], d.pop("postalCodes", UNSET))

        postal_code_areas = cls(
            country=country,
            postal_codes=postal_codes,
        )

        postal_code_areas.additional_properties = d
        return postal_code_areas

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
