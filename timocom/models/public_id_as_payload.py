from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicIDAsPayload")


@_attrs_define
class PublicIDAsPayload:
    """Payload for a public ID.
    The public ID is a unique ID on TIMOCOM side. Used for responses of create requests.

        Attributes:
            id (str | Unset): Alphanumeric unique ID which is used to identify an entity (freight offer, vehicle space
                offer, freight quote) in the TIMOCOM system. Will be generated on TIMOCOM side, only. Example:
                NdKoYeUDQheRB14EeyJzTg.
    """

    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        public_id_as_payload = cls(
            id=id,
        )

        public_id_as_payload.additional_properties = d
        return public_id_as_payload

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
