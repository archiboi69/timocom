from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_object_type import AddressObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_coordinate import GeoCoordinate


T = TypeVar("T", bound="PostalAddress")


@_attrs_define
class PostalAddress:
    """The particulars of the place where an organization is situated.

    Attributes:
        country (str): 2 letter language code as defined by ISO 3166-1 alpha-2.
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
        object_type (AddressObjectType | Unset):
        city (str | Unset):  Example: Gerona.
        geo_coordinate (GeoCoordinate | Unset): Describes a position in longitude and latitude according to WGS84.
        geocoded (bool | Unset): Relevant for responses, only. True if address could be
            geocoded by TIMOCOM. Default: False.
        postal_code (str | Unset):  Example: 17001.
        street_or_postbox (str | Unset):  Example: PO 3454.
    """

    country: str
    object_type: AddressObjectType | Unset = UNSET
    city: str | Unset = UNSET
    geo_coordinate: GeoCoordinate | Unset = UNSET
    geocoded: bool | Unset = False
    postal_code: str | Unset = UNSET
    street_or_postbox: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        object_type: str | Unset = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        city = self.city

        geo_coordinate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geo_coordinate, Unset):
            geo_coordinate = self.geo_coordinate.to_dict()

        geocoded = self.geocoded

        postal_code = self.postal_code

        street_or_postbox = self.street_or_postbox

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
            }
        )
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if city is not UNSET:
            field_dict["city"] = city
        if geo_coordinate is not UNSET:
            field_dict["geoCoordinate"] = geo_coordinate
        if geocoded is not UNSET:
            field_dict["geocoded"] = geocoded
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if street_or_postbox is not UNSET:
            field_dict["streetOrPostbox"] = street_or_postbox

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_coordinate import GeoCoordinate

        d = dict(src_dict)
        country = d.pop("country")

        _object_type = d.pop("objectType", UNSET)
        object_type: AddressObjectType | Unset
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = AddressObjectType(_object_type)

        city = d.pop("city", UNSET)

        _geo_coordinate = d.pop("geoCoordinate", UNSET)
        geo_coordinate: GeoCoordinate | Unset
        if isinstance(_geo_coordinate, Unset):
            geo_coordinate = UNSET
        else:
            geo_coordinate = GeoCoordinate.from_dict(_geo_coordinate)

        geocoded = d.pop("geocoded", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        street_or_postbox = d.pop("streetOrPostbox", UNSET)

        postal_address = cls(
            country=country,
            object_type=object_type,
            city=city,
            geo_coordinate=geo_coordinate,
            geocoded=geocoded,
            postal_code=postal_code,
            street_or_postbox=street_or_postbox,
        )

        postal_address.additional_properties = d
        return postal_address

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
