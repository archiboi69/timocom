from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FreightExchangeResponseMeta")


@_attrs_define
class FreightExchangeResponseMeta:
    """
    Attributes:
        request_id (str | Unset):  Example: 47-11-request-id.
        response_timestamp (datetime.datetime | Unset):  Example: 2022-09-13T13:22:09.3011033Z.
    """

    request_id: str | Unset = UNSET
    response_timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        response_timestamp: str | Unset = UNSET
        if not isinstance(self.response_timestamp, Unset):
            response_timestamp = self.response_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if response_timestamp is not UNSET:
            field_dict["responseTimestamp"] = response_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_id = d.pop("requestId", UNSET)

        _response_timestamp = d.pop("responseTimestamp", UNSET)
        response_timestamp: datetime.datetime | Unset
        if isinstance(_response_timestamp, Unset):
            response_timestamp = UNSET
        else:
            response_timestamp = isoparse(_response_timestamp)

        freight_exchange_response_meta = cls(
            request_id=request_id,
            response_timestamp=response_timestamp,
        )

        freight_exchange_response_meta.additional_properties = d
        return freight_exchange_response_meta

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
