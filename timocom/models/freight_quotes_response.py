from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freight_exchange_response_meta import FreightExchangeResponseMeta
    from ..models.freight_quote import FreightQuote


T = TypeVar("T", bound="FreightQuotesResponse")


@_attrs_define
class FreightQuotesResponse:
    """
    Attributes:
        meta (FreightExchangeResponseMeta | Unset):
        payload (list[FreightQuote] | Unset):
    """

    meta: FreightExchangeResponseMeta | Unset = UNSET
    payload: list[FreightQuote] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        payload: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = []
            for payload_item_data in self.payload:
                payload_item = payload_item_data.to_dict()
                payload.append(payload_item)

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
        from ..models.freight_quote import FreightQuote

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: FreightExchangeResponseMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = FreightExchangeResponseMeta.from_dict(_meta)

        _payload = d.pop("payload", UNSET)
        payload: list[FreightQuote] | Unset = UNSET
        if _payload is not UNSET:
            payload = []
            for payload_item_data in _payload:
                payload_item = FreightQuote.from_dict(payload_item_data)

                payload.append(payload_item)

        freight_quotes_response = cls(
            meta=meta,
            payload=payload,
        )

        freight_quotes_response.additional_properties = d
        return freight_quotes_response

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
