from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GeoCoordinate")


@_attrs_define
class GeoCoordinate:
    """Describes a position in longitude and latitude according to WGS84.

    Attributes:
        longitude (float): The longitude component of a gps Position. Example: 2.82493.
        latitude (float): The latitude component of a gps Position. Example: 41.98311.
    """

    longitude: float
    latitude: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        longitude = self.longitude

        latitude = self.latitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "longitude": longitude,
                "latitude": latitude,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        longitude = d.pop("longitude")

        latitude = d.pop("latitude")

        geo_coordinate = cls(
            longitude=longitude,
            latitude=latitude,
        )

        geo_coordinate.additional_properties = d
        return geo_coordinate

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
