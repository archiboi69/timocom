from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="Area")


@_attrs_define
class Area:
    """Defines the size of the area around an address.

    Attributes:
        address (Address | Unset): The particulars of the place where a freight offer has to be picked up or needs to be
            shipped to. In case of a vehicle offer the address symbolizes the starting point of the vehicle.
        size_km (int | Unset): The amount describes unit and subunit of length in kilometres in a single value. Example:
            55.
    """

    address: Address | Unset = UNSET
    size_km: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        size_km = self.size_km

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if size_km is not UNSET:
            field_dict["size_km"] = size_km

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        size_km = d.pop("size_km", UNSET)

        area = cls(
            address=address,
            size_km=size_km,
        )

        area.additional_properties = d
        return area

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
