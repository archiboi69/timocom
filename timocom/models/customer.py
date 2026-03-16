from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postal_address import PostalAddress


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """A company that is a customer of TIMOCOM. Except for 'id' fields are ignored in publish offer requests.

    Attributes:
        id (int): Unique ID of a customer on TIMOCOM side. Example: 288.
        company_address (PostalAddress | Unset): The particulars of the place where an organization is situated.
        creation_date_time (datetime.datetime | Unset): Filled in response objects, only. Ignored in store
            requests. Example: 2019-08-24T14:15:22Z.
        fax (str | Unset): International Phone Number Example: +49 211 88 26 88 26.
        name (str | Unset): Name of the company. Example: Hernández y Fernández S.A..
        phone (str | Unset): International Phone Number Example: +49 211 88 26 88 26.
        postal_address (PostalAddress | Unset): The particulars of the place where an organization is situated.
        tax_id (str | Unset): Tax ID of the company. Example: TAX-47-87.
    """

    id: int
    company_address: PostalAddress | Unset = UNSET
    creation_date_time: datetime.datetime | Unset = UNSET
    fax: str | Unset = UNSET
    name: str | Unset = UNSET
    phone: str | Unset = UNSET
    postal_address: PostalAddress | Unset = UNSET
    tax_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company_address, Unset):
            company_address = self.company_address.to_dict()

        creation_date_time: str | Unset = UNSET
        if not isinstance(self.creation_date_time, Unset):
            creation_date_time = self.creation_date_time.isoformat()

        fax = self.fax

        name = self.name

        phone = self.phone

        postal_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.postal_address, Unset):
            postal_address = self.postal_address.to_dict()

        tax_id = self.tax_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if company_address is not UNSET:
            field_dict["companyAddress"] = company_address
        if creation_date_time is not UNSET:
            field_dict["creationDateTime"] = creation_date_time
        if fax is not UNSET:
            field_dict["fax"] = fax
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if postal_address is not UNSET:
            field_dict["postalAddress"] = postal_address
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.postal_address import PostalAddress

        d = dict(src_dict)
        id = d.pop("id")

        _company_address = d.pop("companyAddress", UNSET)
        company_address: PostalAddress | Unset
        if isinstance(_company_address, Unset):
            company_address = UNSET
        else:
            company_address = PostalAddress.from_dict(_company_address)

        _creation_date_time = d.pop("creationDateTime", UNSET)
        creation_date_time: datetime.datetime | Unset
        if isinstance(_creation_date_time, Unset):
            creation_date_time = UNSET
        else:
            creation_date_time = isoparse(_creation_date_time)

        fax = d.pop("fax", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        _postal_address = d.pop("postalAddress", UNSET)
        postal_address: PostalAddress | Unset
        if isinstance(_postal_address, Unset):
            postal_address = UNSET
        else:
            postal_address = PostalAddress.from_dict(_postal_address)

        tax_id = d.pop("taxId", UNSET)

        customer = cls(
            id=id,
            company_address=company_address,
            creation_date_time=creation_date_time,
            fax=fax,
            name=name,
            phone=phone,
            postal_address=postal_address,
            tax_id=tax_id,
        )

        customer.additional_properties = d
        return customer

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
