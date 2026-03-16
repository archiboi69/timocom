from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualDates")


@_attrs_define
class IndividualDates:
    """List of dates (logically composed by a disjunction), compared with loading interval/date (cargo) respective start
    date (truck). At least one and up to 5 date elements must be set.

        Attributes:
            object_type (str | Unset):
            dates (list[datetime.date] | Unset):
    """

    object_type: str | Unset = UNSET
    dates: list[datetime.date] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        dates: list[str] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.isoformat()
                dates.append(dates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if dates is not UNSET:
            field_dict["dates"] = dates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("objectType", UNSET)

        _dates = d.pop("dates", UNSET)
        dates: list[datetime.date] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = isoparse(dates_item_data).date()

                dates.append(dates_item)

        individual_dates = cls(
            object_type=object_type,
            dates=dates,
        )

        individual_dates.additional_properties = d
        return individual_dates

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
