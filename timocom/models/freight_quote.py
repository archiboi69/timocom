from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_person import ContactPerson
    from ..models.customer import Customer
    from ..models.money import Money


T = TypeVar("T", bound="FreightQuote")


@_attrs_define
class FreightQuote:
    """
    Attributes:
        offer_id (str):
        price (Money): A monetary amount specified in a particular currency.
        expiration_date_time (datetime.datetime):
        contact_person (ContactPerson): A contact person describes who can be contacted by interested parties via which
            communication channels. A contact person is sent within an offer and is disposed when the offer is deleted or
            expires. The data is nowhere else referenceable or usable in the TIMOCOM Marketplace.
        customer (Customer): A company that is a customer of TIMOCOM. Except for 'id' fields are ignored in publish
            offer requests.
        id (str | Unset): Alphanumeric unique ID which is used to identify an entity (freight offer, vehicle space
            offer, freight quote) in the TIMOCOM system. Will be generated on TIMOCOM side, only. Example:
            NdKoYeUDQheRB14EeyJzTg.
        status (str | Unset): * ACTIVE
            * ACCEPTED
            * REJECTED
            * WITHDRAWN
            * EXPIRED
        public_remark (str | Unset):
    """

    offer_id: str
    price: Money
    expiration_date_time: datetime.datetime
    contact_person: ContactPerson
    customer: Customer
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    public_remark: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offer_id = self.offer_id

        price = self.price.to_dict()

        expiration_date_time = self.expiration_date_time.isoformat()

        contact_person = self.contact_person.to_dict()

        customer = self.customer.to_dict()

        id = self.id

        status = self.status

        public_remark = self.public_remark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offerId": offer_id,
                "price": price,
                "expirationDateTime": expiration_date_time,
                "contactPerson": contact_person,
                "customer": customer,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if public_remark is not UNSET:
            field_dict["publicRemark"] = public_remark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_person import ContactPerson
        from ..models.customer import Customer
        from ..models.money import Money

        d = dict(src_dict)
        offer_id = d.pop("offerId")

        price = Money.from_dict(d.pop("price"))

        expiration_date_time = isoparse(d.pop("expirationDateTime"))

        contact_person = ContactPerson.from_dict(d.pop("contactPerson"))

        customer = Customer.from_dict(d.pop("customer"))

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        public_remark = d.pop("publicRemark", UNSET)

        freight_quote = cls(
            offer_id=offer_id,
            price=price,
            expiration_date_time=expiration_date_time,
            contact_person=contact_person,
            customer=customer,
            id=id,
            status=status,
            public_remark=public_remark,
        )

        freight_quote.additional_properties = d
        return freight_quote

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
