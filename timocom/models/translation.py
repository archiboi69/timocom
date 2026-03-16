from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Translation")


@_attrs_define
class Translation:
    """Translation of a value into a specific language.

    Attributes:
        value (str | Unset): The translated value.
        language (str | Unset): 2 letter language code as defined by ISO-639.
            Currently supported values:
            * af
            * ar
            * az
            * be
            * bg
            * bs
            * ca
            * ce
            * co
            * cs
            * da
            * de
            * el
            * en
            * eo
            * es
            * et
            * eu
            * fa
            * fi
            * fo
            * fr
            * fy
            * ga
            * gd
            * gl
            * he
            * hr
            * hu
            * hy
            * id
            * is
            * it
            * ja
            * ka
            * kk
            * ku
            * kw
            * ky
            * lb
            * li
            * lt
            * lv
            * mk
            * mn
            * mt
            * nl
            * no
            * oc
            * pl
            * ps
            * pt
            * rm
            * ro
            * ru
            * sc
            * sk
            * sl
            * sq
            * sr
            * sv
            * sw
            * th
            * tr
            * uk
            * uz
            * vi
            * wa
            * zh Example: de.
    """

    value: str | Unset = UNSET
    language: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        language = d.pop("language", UNSET)

        translation = cls(
            value=value,
            language=language,
        )

        translation.additional_properties = d
        return translation

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
