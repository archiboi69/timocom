from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleSpaceDestinationCountries")


@_attrs_define
class VehicleSpaceDestinationCountries:
    """W/o wrapping of the countries list, no model class (in Java) which implements the interface
    VehicleSpaceDestinationChoice would be generated.

        Attributes:
            object_type (str | Unset):
            countries (list[str] | Unset):
    """

    object_type: str | Unset = UNSET
    countries: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if countries is not UNSET:
            field_dict["countries"] = countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("objectType", UNSET)

        countries = cast(list[str], d.pop("countries", UNSET))

        vehicle_space_destination_countries = cls(
            object_type=object_type,
            countries=countries,
        )

        vehicle_space_destination_countries.additional_properties = d
        return vehicle_space_destination_countries

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
