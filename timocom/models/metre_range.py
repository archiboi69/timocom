from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetreRange")


@_attrs_define
class MetreRange:
    """Filter criteria that can be defined to find offers which length is within the defined range.

    Attributes:
        inclusive_minimum (float | Unset): The amount describes unit and subunit of length in metres in a single value,
            where the integer part (digits before the decimal point) is for the major unit and fractional part (digits after
            the decimal point) is for the minor unit. Example: 12.31.
        inclusive_maximum (float | Unset): The amount describes unit and subunit of length in metres in a single value,
            where the integer part (digits before the decimal point) is for the major unit and fractional part (digits after
            the decimal point) is for the minor unit. Example: 12.31.
    """

    inclusive_minimum: float | Unset = UNSET
    inclusive_maximum: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inclusive_minimum = self.inclusive_minimum

        inclusive_maximum = self.inclusive_maximum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inclusive_minimum is not UNSET:
            field_dict["inclusiveMinimum"] = inclusive_minimum
        if inclusive_maximum is not UNSET:
            field_dict["inclusiveMaximum"] = inclusive_maximum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inclusive_minimum = d.pop("inclusiveMinimum", UNSET)

        inclusive_maximum = d.pop("inclusiveMaximum", UNSET)

        metre_range = cls(
            inclusive_minimum=inclusive_minimum,
            inclusive_maximum=inclusive_maximum,
        )

        metre_range.additional_properties = d
        return metre_range

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
