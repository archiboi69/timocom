from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactPerson")


@_attrs_define
class ContactPerson:
    """A contact person describes who can be contacted by interested parties via which communication channels. A contact
    person is sent within an offer and is disposed when the offer is deleted or expires. The data is nowhere else
    referenceable or usable in the TIMOCOM Marketplace.

        Attributes:
            email (str): E-mail address of the contact person. Example: schnittstellen@timocom.com.
            first_name (str): First name of the contact person. Example: Fernández.
            languages (list[str]): List of languages the contact person speaks and wants to be contacted.
            last_name (str): Last name of the contact person. Example: Hernández.
            title (str): Form of address of the contact person e.g.:
                - MR
                - MRS Example: MR.
            business_phone (str | Unset): International Phone Number Example: +49 211 88 26 88 26.
            fax (str | Unset): International Phone Number Example: +49 211 88 26 88 26.
            mobile_phone (str | Unset): International Phone Number Example: +49 211 88 26 88 26.
    """

    email: str
    first_name: str
    languages: list[str]
    last_name: str
    title: str
    business_phone: str | Unset = UNSET
    fax: str | Unset = UNSET
    mobile_phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        languages = self.languages

        last_name = self.last_name

        title = self.title

        business_phone = self.business_phone

        fax = self.fax

        mobile_phone = self.mobile_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "languages": languages,
                "lastName": last_name,
                "title": title,
            }
        )
        if business_phone is not UNSET:
            field_dict["businessPhone"] = business_phone
        if fax is not UNSET:
            field_dict["fax"] = fax
        if mobile_phone is not UNSET:
            field_dict["mobilePhone"] = mobile_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        first_name = d.pop("firstName")

        languages = cast(list[str], d.pop("languages"))

        last_name = d.pop("lastName")

        title = d.pop("title")

        business_phone = d.pop("businessPhone", UNSET)

        fax = d.pop("fax", UNSET)

        mobile_phone = d.pop("mobilePhone", UNSET)

        contact_person = cls(
            email=email,
            first_name=first_name,
            languages=languages,
            last_name=last_name,
            title=title,
            business_phone=business_phone,
            fax=fax,
            mobile_phone=mobile_phone,
        )

        contact_person.additional_properties = d
        return contact_person

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
