from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area import Area


T = TypeVar("T", bound="VehicleSpaceDestinationArea")


@_attrs_define
class VehicleSpaceDestinationArea:
    """
    Attributes:
        object_type (str | Unset):
        area (Area | Unset): Defines the size of the area around an address.
    """

    object_type: str | Unset = UNSET
    area: Area | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area import Area

        d = dict(src_dict)
        object_type = d.pop("objectType", UNSET)

        _area = d.pop("area", UNSET)
        area: Area | Unset
        if isinstance(_area, Unset):
            area = UNSET
        else:
            area = Area.from_dict(_area)

        vehicle_space_destination_area = cls(
            object_type=object_type,
            area=area,
        )

        vehicle_space_destination_area.additional_properties = d
        return vehicle_space_destination_area

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
