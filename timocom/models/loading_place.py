from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.loading_place_loading_type import LoadingPlaceLoadingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="LoadingPlace")


@_attrs_define
class LoadingPlace:
    """A place where freight is loaded or unloaded.

    Attributes:
        loading_type (LoadingPlaceLoadingType): Loading type. Must be LOADING for first loading
            place and UNLOADING for last loading place. Example: LOADING.
        earliest_loading_date (datetime.date): Earliest (un)loading date of the loading place. If no value is known, it
            is recommended to set it to the value of the ‘latestLoadingDate’. Example: 2019-08-24.
        latest_loading_date (datetime.date): Latest (un)loading date of the loading place. Mandatory field in first
            loading place (start place). Example: 2019-08-26.
        address (Address | Unset): The particulars of the place where a freight offer has to be picked up or needs to be
            shipped to. In case of a vehicle offer the address symbolizes the starting point of the vehicle.
        start_time (str | Unset): (Un)loading start time of the loading place. Example: 08:15.
        end_time (str | Unset): (Un)loading end time of the loading place. Example: 17:15.
    """

    loading_type: LoadingPlaceLoadingType
    earliest_loading_date: datetime.date
    latest_loading_date: datetime.date
    address: Address | Unset = UNSET
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loading_type = self.loading_type.value

        earliest_loading_date = self.earliest_loading_date.isoformat()

        latest_loading_date = self.latest_loading_date.isoformat()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "loadingType": loading_type,
                "earliestLoadingDate": earliest_loading_date,
                "latestLoadingDate": latest_loading_date,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address

        d = dict(src_dict)
        loading_type = LoadingPlaceLoadingType(d.pop("loadingType"))

        earliest_loading_date = isoparse(d.pop("earliestLoadingDate")).date()

        latest_loading_date = isoparse(d.pop("latestLoadingDate")).date()

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        loading_place = cls(
            loading_type=loading_type,
            earliest_loading_date=earliest_loading_date,
            latest_loading_date=latest_loading_date,
            address=address,
            start_time=start_time,
            end_time=end_time,
        )

        loading_place.additional_properties = d
        return loading_place

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
