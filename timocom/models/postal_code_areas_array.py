from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postal_code_areas import PostalCodeAreas


T = TypeVar("T", bound="PostalCodeAreasArray")


@_attrs_define
class PostalCodeAreasArray:
    """An array of postal code areas (Mandatory list ensures instantiation of impl class).

    Attributes:
        object_type (str | Unset):
        postal_code_areas (list[PostalCodeAreas] | Unset):
    """

    object_type: str | Unset = UNSET
    postal_code_areas: list[PostalCodeAreas] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        postal_code_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.postal_code_areas, Unset):
            postal_code_areas = []
            for postal_code_areas_item_data in self.postal_code_areas:
                postal_code_areas_item = postal_code_areas_item_data.to_dict()
                postal_code_areas.append(postal_code_areas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if postal_code_areas is not UNSET:
            field_dict["postalCodeAreas"] = postal_code_areas

        field_dict['objectType'] = 'postalCodeAreasArray'
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.postal_code_areas import PostalCodeAreas

        d = dict(src_dict)
        object_type = d.pop("objectType", UNSET)

        _postal_code_areas = d.pop("postalCodeAreas", UNSET)
        postal_code_areas: list[PostalCodeAreas] | Unset = UNSET
        if _postal_code_areas is not UNSET:
            postal_code_areas = []
            for postal_code_areas_item_data in _postal_code_areas:
                postal_code_areas_item = PostalCodeAreas.from_dict(postal_code_areas_item_data)

                postal_code_areas.append(postal_code_areas_item)

        postal_code_areas_array = cls(
            object_type=object_type,
            postal_code_areas=postal_code_areas,
        )

        postal_code_areas_array.additional_properties = d
        return postal_code_areas_array

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
