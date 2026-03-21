from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.closed_freight_exchange_setting import ClosedFreightExchangeSetting
    from ..models.contact_person import ContactPerson
    from ..models.customer import Customer
    from ..models.loading_place import LoadingPlace
    from ..models.money import Money
    from ..models.vehicle_properties import VehicleProperties


T = TypeVar("T", bound="FreightOffer")


@_attrs_define
class FreightOffer:
    """A freight offer that is published within the freight exchange indicates a demand for transportation. It contains
    information related to the goods to be transported. distance_km field is set in result of a search request, only.

        Attributes:
            contact_person (ContactPerson): A contact person describes who can be contacted by interested parties via which
                communication channels. A contact person is sent within an offer and is disposed when the offer is deleted or
                expires. The data is nowhere else referenceable or usable in the TIMOCOM Marketplace.
            trackable (bool): Localisation with TIMOCOM Tracking available.
            vehicle_properties (VehicleProperties): Generic type used to describe the properties of a certain vehicle with
                its values.
            accept_quotes (bool): Shows that a quote is/was accepted.
            freight_description (str): Description of the freight. Example: Mandatory further description of the freight.
            length_m (float): The amount describes unit and subunit of length in metres in a single value, where the integer
                part (digits before the decimal point) is for the major unit and fractional part (digits after the decimal
                point) is for the minor unit. Example: 12.31.
            loading_places (list[LoadingPlace]): Loading places of the freight.
            weight_t (float): The amount describes unit and subunit of weight in tons in a single value, where the integer
                part (digits before the decimal point) is for the major unit and fractional part (digits after the decimal
                point) is for the minor unit. Example: 5.55.
            closed_freight_exchange_setting (ClosedFreightExchangeSetting | Unset): The Closed Freight Exchange (briefly
                CFE, or in German: Geschlossene Frachtenbörse) is a concept of grouping TIMOCOM customers for offer publication
                constraints purposes. The common use case is that an offer with CFE settings will be published exclusively
                within the CFE in the first place. This means that it is not visible to any TIMOCOM customer which is not member
                of the set CFE. After a set duration of time (maybe never) it will be automatically visible to all TIMOCOM
                customers unless it has not been withdrawn before.

                If your company has a valid CFE contract with TIMOCOM you are able to send via the API all Closed Freight
                Exchange settings with the submitted offer.
            creation_date_time (datetime.datetime | Unset): Filled in response objects, only. Ignored in store
                requests. Example: 2019-08-24T14:15:22Z.
            customer (Customer | Unset): A company that is a customer of TIMOCOM. Except for 'id' fields are ignored in
                publish offer requests.
            deeplink (str | Unset): URL deep link to the TIMOCOM offer details. Will be set by TIMOCOM and in search
                results, only. Example: https://timocom.com/example/freight/hggaXk77z.
            excluded_customers (list[int] | Unset): List of customer timocomIds that are excluded from
                seeing the offer. List may be empty. The list is limited to 1000 entries.
            id (str | Unset): Unique ID on TIMOCOM side. Only set in result of a
                search request. Example: offer-471-publicId.
            internal_remark (str | Unset): Remark, internally visible for users of the publishing customer. Example: This
                remark is visible to users of your company, only.
            logistics_document_types (list[str] | Unset): Vehicle/freight documents e.g.
                * GMP_CERTIFICATE
            public_remark (str | Unset): Remark, publicly visible within the offer. Example: This remark is visible to all.
            use_messenger (bool | Unset): If set to true, the login email address for the TIMOCOM Marketplace must be
                specified in the contact person. The email is used to assign the user to the offer. Example: True.
            additional_information (list[str] | Unset): Additional information about the goods.
            distance_km (int | Unset): The amount describes unit and subunit of length in kilometres in a single value.
                Example: 55.
            payment_due_within_days (int | Unset): Payment is due within specified number of days. Example: 30.
            price (Money | Unset): A monetary amount specified in a particular currency.
    """

    contact_person: ContactPerson
    trackable: bool
    vehicle_properties: VehicleProperties
    accept_quotes: bool
    freight_description: str
    length_m: float
    loading_places: list[LoadingPlace]
    weight_t: float
    closed_freight_exchange_setting: ClosedFreightExchangeSetting | Unset = UNSET
    creation_date_time: datetime.datetime | Unset = UNSET
    customer: Customer | Unset = UNSET
    deeplink: str | Unset = UNSET
    excluded_customers: list[int] | Unset = UNSET
    id: str | Unset = UNSET
    internal_remark: str | Unset = UNSET
    logistics_document_types: list[str] | Unset = UNSET
    public_remark: str | Unset = UNSET
    use_messenger: bool | Unset = UNSET
    additional_information: list[str] | Unset = UNSET
    distance_km: int | Unset = UNSET
    payment_due_within_days: int | Unset = UNSET
    price: Money | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_person = self.contact_person.to_dict()

        trackable = self.trackable

        vehicle_properties = self.vehicle_properties.to_dict()

        accept_quotes = self.accept_quotes

        freight_description = self.freight_description

        length_m = self.length_m

        loading_places = []
        for loading_places_item_data in self.loading_places:
            loading_places_item = loading_places_item_data.to_dict()
            loading_places.append(loading_places_item)

        weight_t = self.weight_t

        closed_freight_exchange_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.closed_freight_exchange_setting, Unset):
            closed_freight_exchange_setting = self.closed_freight_exchange_setting.to_dict()

        creation_date_time: str | Unset = UNSET
        if not isinstance(self.creation_date_time, Unset):
            creation_date_time = self.creation_date_time.isoformat()

        customer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        deeplink = self.deeplink

        excluded_customers: list[int] | Unset = UNSET
        if not isinstance(self.excluded_customers, Unset):
            excluded_customers = self.excluded_customers

        id = self.id

        internal_remark = self.internal_remark

        logistics_document_types: list[str] | Unset = UNSET
        if not isinstance(self.logistics_document_types, Unset):
            logistics_document_types = self.logistics_document_types

        public_remark = self.public_remark

        use_messenger = self.use_messenger

        additional_information: list[str] | Unset = UNSET
        if not isinstance(self.additional_information, Unset):
            additional_information = self.additional_information

        distance_km = self.distance_km

        payment_due_within_days = self.payment_due_within_days

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactPerson": contact_person,
                "trackable": trackable,
                "vehicleProperties": vehicle_properties,
                "acceptQuotes": accept_quotes,
                "freightDescription": freight_description,
                "length_m": length_m,
                "loadingPlaces": loading_places,
                "weight_t": weight_t,
            }
        )
        if closed_freight_exchange_setting is not UNSET:
            field_dict["closedFreightExchangeSetting"] = closed_freight_exchange_setting
        if creation_date_time is not UNSET:
            field_dict["creationDateTime"] = creation_date_time
        if customer is not UNSET:
            field_dict["customer"] = customer
        if deeplink is not UNSET:
            field_dict["deeplink"] = deeplink
        if excluded_customers is not UNSET:
            field_dict["excludedCustomers"] = excluded_customers
        if id is not UNSET:
            field_dict["id"] = id
        if internal_remark is not UNSET:
            field_dict["internalRemark"] = internal_remark
        if logistics_document_types is not UNSET:
            field_dict["logisticsDocumentTypes"] = logistics_document_types
        if public_remark is not UNSET:
            field_dict["publicRemark"] = public_remark
        if use_messenger is not UNSET:
            field_dict["useMessenger"] = use_messenger
        if additional_information is not UNSET:
            field_dict["additionalInformation"] = additional_information
        if distance_km is not UNSET:
            field_dict["distance_km"] = distance_km
        if payment_due_within_days is not UNSET:
            field_dict["paymentDueWithinDays"] = payment_due_within_days
        if price is not UNSET:
            field_dict["price"] = price

        field_dict['objectType'] = 'freightOffer'
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.closed_freight_exchange_setting import ClosedFreightExchangeSetting
        from ..models.contact_person import ContactPerson
        from ..models.customer import Customer
        from ..models.loading_place import LoadingPlace
        from ..models.money import Money
        from ..models.vehicle_properties import VehicleProperties

        d = dict(src_dict)
        contact_person = ContactPerson.from_dict(d.pop("contactPerson"))

        trackable = d.pop("trackable")

        vehicle_properties = VehicleProperties.from_dict(d.pop("vehicleProperties"))

        accept_quotes = d.pop("acceptQuotes")

        freight_description = d.pop("freightDescription")

        length_m = d.pop("length_m")

        loading_places = []
        _loading_places = d.pop("loadingPlaces")
        for loading_places_item_data in _loading_places:
            loading_places_item = LoadingPlace.from_dict(loading_places_item_data)

            loading_places.append(loading_places_item)

        weight_t = d.pop("weight_t")

        _closed_freight_exchange_setting = d.pop("closedFreightExchangeSetting", UNSET)
        closed_freight_exchange_setting: ClosedFreightExchangeSetting | Unset
        if isinstance(_closed_freight_exchange_setting, Unset):
            closed_freight_exchange_setting = UNSET
        else:
            closed_freight_exchange_setting = ClosedFreightExchangeSetting.from_dict(_closed_freight_exchange_setting)

        _creation_date_time = d.pop("creationDateTime", UNSET)
        creation_date_time: datetime.datetime | Unset
        if isinstance(_creation_date_time, Unset):
            creation_date_time = UNSET
        else:
            creation_date_time = isoparse(_creation_date_time)

        _customer = d.pop("customer", UNSET)
        customer: Customer | Unset
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = Customer.from_dict(_customer)

        deeplink = d.pop("deeplink", UNSET)

        excluded_customers = cast(list[int], d.pop("excludedCustomers", UNSET))

        id = d.pop("id", UNSET)

        internal_remark = d.pop("internalRemark", UNSET)

        logistics_document_types = cast(list[str], d.pop("logisticsDocumentTypes", UNSET))

        public_remark = d.pop("publicRemark", UNSET)

        use_messenger = d.pop("useMessenger", UNSET)

        additional_information = cast(list[str], d.pop("additionalInformation", UNSET))

        distance_km = d.pop("distance_km", UNSET)

        payment_due_within_days = d.pop("paymentDueWithinDays", UNSET)

        _price = d.pop("price", UNSET)
        price: Money | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Money.from_dict(_price)

        freight_offer = cls(
            contact_person=contact_person,
            trackable=trackable,
            vehicle_properties=vehicle_properties,
            accept_quotes=accept_quotes,
            freight_description=freight_description,
            length_m=length_m,
            loading_places=loading_places,
            weight_t=weight_t,
            closed_freight_exchange_setting=closed_freight_exchange_setting,
            creation_date_time=creation_date_time,
            customer=customer,
            deeplink=deeplink,
            excluded_customers=excluded_customers,
            id=id,
            internal_remark=internal_remark,
            logistics_document_types=logistics_document_types,
            public_remark=public_remark,
            use_messenger=use_messenger,
            additional_information=additional_information,
            distance_km=distance_km,
            payment_due_within_days=payment_due_within_days,
            price=price,
        )

        freight_offer.additional_properties = d
        return freight_offer

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
