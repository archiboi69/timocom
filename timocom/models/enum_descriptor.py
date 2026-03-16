from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.translation import Translation


T = TypeVar("T", bound="EnumDescriptor")


@_attrs_define
class EnumDescriptor:
    """Describes a reference value and its translations into different languages.

    Attributes:
        value (str | Unset): The referenced value.
        since (str | Unset): The date when the value was introduced. Format YYYY-MM.
        translations (list[Translation] | Unset):
    """

    value: str | Unset = UNSET
    since: str | Unset = UNSET
    translations: list[Translation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        since = self.since

        translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if since is not UNSET:
            field_dict["since"] = since
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translation import Translation

        d = dict(src_dict)
        value = d.pop("value", UNSET)

        since = d.pop("since", UNSET)

        _translations = d.pop("translations", UNSET)
        translations: list[Translation] | Unset = UNSET
        if _translations is not UNSET:
            translations = []
            for translations_item_data in _translations:
                translations_item = Translation.from_dict(translations_item_data)

                translations.append(translations_item)

        enum_descriptor = cls(
            value=value,
            since=since,
            translations=translations,
        )

        enum_descriptor.additional_properties = d
        return enum_descriptor

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
