from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freight_exchange_response_meta import FreightExchangeResponseMeta
    from ..models.public_id_as_payload import PublicIDAsPayload


T = TypeVar("T", bound="CreateResourceResponse")


@_attrs_define
class CreateResourceResponse:
    """
    Attributes:
        meta (FreightExchangeResponseMeta | Unset):
        payload (PublicIDAsPayload | Unset): Payload for a public ID.
            The public ID is a unique ID on TIMOCOM side. Used for responses of create requests.
    """

    meta: FreightExchangeResponseMeta | Unset = UNSET
    payload: PublicIDAsPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freight_exchange_response_meta import FreightExchangeResponseMeta
        from ..models.public_id_as_payload import PublicIDAsPayload

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: FreightExchangeResponseMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = FreightExchangeResponseMeta.from_dict(_meta)

        _payload = d.pop("payload", UNSET)
        payload: PublicIDAsPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = PublicIDAsPayload.from_dict(_payload)

        create_resource_response = cls(
            meta=meta,
            payload=payload,
        )

        create_resource_response.additional_properties = d
        return create_resource_response

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
