from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateInterval")


@_attrs_define
class DateInterval:
    """Any of the dates within this interval.

    Attributes:
        object_type (str | Unset):
        start (datetime.date | Unset): Left lower bound (inclusive). Example: 2019-08-24.
        end (datetime.date | Unset): Right upper bound (inclusive).
             Example: 2019-08-27.
    """

    object_type: str | Unset = UNSET
    start: datetime.date | Unset = UNSET
    end: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("objectType", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.date | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start).date()

        _end = d.pop("end", UNSET)
        end: datetime.date | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end).date()

        date_interval = cls(
            object_type=object_type,
            start=start,
            end=end,
        )

        date_interval.additional_properties = d
        return date_interval

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
