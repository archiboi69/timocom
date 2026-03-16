from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.closed_freight_exchange_setting import ClosedFreightExchangeSetting
    from ..models.contact_person import ContactPerson
    from ..models.customer import Customer
    from ..models.vehicle_properties import VehicleProperties
    from ..models.vehicle_space_destination_area import VehicleSpaceDestinationArea
    from ..models.vehicle_space_destination_countries import VehicleSpaceDestinationCountries


T = TypeVar("T", bound="VehicleSpaceOffer")


@_attrs_define
class VehicleSpaceOffer:
    """A vehicle space offer that is published within the freight exchange indicates available vehicle space. It contains
    information related to available vehicle.

    * The Sum of truckLength_m and trailerLength_m has to be greater than 0.
    * The Sum of truckWeight_t and trailerWeight_t has to be greater than 0.

        Attributes:
            contact_person (ContactPerson): A contact person describes who can be contacted by interested parties via which
                communication channels. A contact person is sent within an offer and is disposed when the offer is deleted or
                expires. The data is nowhere else referenceable or usable in the TIMOCOM Marketplace.
            trackable (bool): Localisation with TIMOCOM Tracking available.
            vehicle_properties (VehicleProperties): Generic type used to describe the properties of a certain vehicle with
                its values.
            start (Address): The particulars of the place where a freight offer has to be picked up or needs to be shipped
                to. In case of a vehicle offer the address symbolizes the starting point of the vehicle.
            destination (VehicleSpaceDestinationArea | VehicleSpaceDestinationCountries): The destination area of a vehicle
                space.
            loading_date (datetime.date): Loading date (current date + max 31 days).
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
            trailer_length_m (float | Unset): The amount describes unit and subunit of length in metres in a single value,
                where the integer part (digits before the decimal point) is for the major unit and fractional part (digits after
                the decimal point) is for the minor unit. Example: 12.31.
            truck_length_m (float | Unset): The amount describes unit and subunit of length in metres in a single value,
                where the integer part (digits before the decimal point) is for the major unit and fractional part (digits after
                the decimal point) is for the minor unit. Example: 12.31.
            trailer_weight_t (float | Unset): The amount describes unit and subunit of weight in tons in a single value,
                where the integer part (digits before the decimal point) is for the major unit and fractional part (digits after
                the decimal point) is for the minor unit. Example: 5.55.
            truck_weight_t (float | Unset): The amount describes unit and subunit of weight in tons in a single value, where
                the integer part (digits before the decimal point) is for the major unit and fractional part (digits after the
                decimal point) is for the minor unit. Example: 5.55.
    """

    contact_person: ContactPerson
    trackable: bool
    vehicle_properties: VehicleProperties
    start: Address
    destination: VehicleSpaceDestinationArea | VehicleSpaceDestinationCountries
    loading_date: datetime.date
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
    trailer_length_m: float | Unset = UNSET
    truck_length_m: float | Unset = UNSET
    trailer_weight_t: float | Unset = UNSET
    truck_weight_t: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.vehicle_space_destination_area import VehicleSpaceDestinationArea

        contact_person = self.contact_person.to_dict()

        trackable = self.trackable

        vehicle_properties = self.vehicle_properties.to_dict()

        start = self.start.to_dict()

        destination: dict[str, Any]
        if isinstance(self.destination, VehicleSpaceDestinationArea):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        loading_date = self.loading_date.isoformat()

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

        trailer_length_m = self.trailer_length_m

        truck_length_m = self.truck_length_m

        trailer_weight_t = self.trailer_weight_t

        truck_weight_t = self.truck_weight_t

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactPerson": contact_person,
                "trackable": trackable,
                "vehicleProperties": vehicle_properties,
                "start": start,
                "destination": destination,
                "loadingDate": loading_date,
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
        if trailer_length_m is not UNSET:
            field_dict["trailerLength_m"] = trailer_length_m
        if truck_length_m is not UNSET:
            field_dict["truckLength_m"] = truck_length_m
        if trailer_weight_t is not UNSET:
            field_dict["trailerWeight_t"] = trailer_weight_t
        if truck_weight_t is not UNSET:
            field_dict["truckWeight_t"] = truck_weight_t

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.closed_freight_exchange_setting import ClosedFreightExchangeSetting
        from ..models.contact_person import ContactPerson
        from ..models.customer import Customer
        from ..models.vehicle_properties import VehicleProperties
        from ..models.vehicle_space_destination_area import VehicleSpaceDestinationArea
        from ..models.vehicle_space_destination_countries import VehicleSpaceDestinationCountries

        d = dict(src_dict)
        contact_person = ContactPerson.from_dict(d.pop("contactPerson"))

        trackable = d.pop("trackable")

        vehicle_properties = VehicleProperties.from_dict(d.pop("vehicleProperties"))

        start = Address.from_dict(d.pop("start"))

        def _parse_destination(data: object) -> VehicleSpaceDestinationArea | VehicleSpaceDestinationCountries:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasvehicle_space_destination_choice_type_0 = VehicleSpaceDestinationArea.from_dict(data)

                return componentsschemasvehicle_space_destination_choice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasvehicle_space_destination_choice_type_1 = VehicleSpaceDestinationCountries.from_dict(data)

            return componentsschemasvehicle_space_destination_choice_type_1

        destination = _parse_destination(d.pop("destination"))

        loading_date = isoparse(d.pop("loadingDate")).date()

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

        trailer_length_m = d.pop("trailerLength_m", UNSET)

        truck_length_m = d.pop("truckLength_m", UNSET)

        trailer_weight_t = d.pop("trailerWeight_t", UNSET)

        truck_weight_t = d.pop("truckWeight_t", UNSET)

        vehicle_space_offer = cls(
            contact_person=contact_person,
            trackable=trackable,
            vehicle_properties=vehicle_properties,
            start=start,
            destination=destination,
            loading_date=loading_date,
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
            trailer_length_m=trailer_length_m,
            truck_length_m=truck_length_m,
            trailer_weight_t=trailer_weight_t,
            truck_weight_t=truck_weight_t,
        )

        vehicle_space_offer.additional_properties = d
        return vehicle_space_offer

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
