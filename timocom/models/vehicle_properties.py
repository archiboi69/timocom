from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleProperties")


@_attrs_define
class VehicleProperties:
    """Generic type used to describe the properties of a certain vehicle with its values.

    Attributes:
        body (list[str]): At least one value is required.
        type_ (list[str]): Exactly one value is required for vehicle space and at least one value is required for
            freight.
        body_property (list[str] | Unset):
        equipment (list[str] | Unset): Special equipment that might be required to carry out a transport.
        load_securing (list[str] | Unset):
        swap_body (list[str] | Unset):
    """

    body: list[str]
    type_: list[str]
    body_property: list[str] | Unset = UNSET
    equipment: list[str] | Unset = UNSET
    load_securing: list[str] | Unset = UNSET
    swap_body: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        type_ = self.type_

        body_property: list[str] | Unset = UNSET
        if not isinstance(self.body_property, Unset):
            body_property = self.body_property

        equipment: list[str] | Unset = UNSET
        if not isinstance(self.equipment, Unset):
            equipment = self.equipment

        load_securing: list[str] | Unset = UNSET
        if not isinstance(self.load_securing, Unset):
            load_securing = self.load_securing

        swap_body: list[str] | Unset = UNSET
        if not isinstance(self.swap_body, Unset):
            swap_body = self.swap_body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "type": type_,
            }
        )
        if body_property is not UNSET:
            field_dict["bodyProperty"] = body_property
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if load_securing is not UNSET:
            field_dict["loadSecuring"] = load_securing
        if swap_body is not UNSET:
            field_dict["swapBody"] = swap_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = cast(list[str], d.pop("body"))

        type_ = cast(list[str], d.pop("type"))

        body_property = cast(list[str], d.pop("bodyProperty", UNSET))

        equipment = cast(list[str], d.pop("equipment", UNSET))

        load_securing = cast(list[str], d.pop("loadSecuring", UNSET))

        swap_body = cast(list[str], d.pop("swapBody", UNSET))

        vehicle_properties = cls(
            body=body,
            type_=type_,
            body_property=body_property,
            equipment=equipment,
            load_securing=load_securing,
            swap_body=swap_body,
        )

        vehicle_properties.additional_properties = d
        return vehicle_properties

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
