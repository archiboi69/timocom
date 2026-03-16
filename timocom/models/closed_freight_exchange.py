from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.closed_freight_exchange_publication_type import ClosedFreightExchangePublicationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClosedFreightExchange")


@_attrs_define
class ClosedFreightExchange:
    """The Closed Freight Exchange (briefly CFE, or in German: Geschlossene Frachtenbörse) is a concept of grouping TIMOCOM
    customers for offer publication constraints purposes. The common use case is that an offer with CFE settings will be
    published exclusively within the CFE in the first place. This means that it is not visible to any TIMOCOM customer
    which is not member of the set CFE. After a set duration of time (maybe never) it will be automatically visible to
    all TIMOCOM customers unless it has not been withdrawn before.

    If your company has a valid CFE contract with TIMOCOM you are able to query for all CFE your TIMOCOM ID is part of.

        Attributes:
            closed_freight_exchange_id (int): Unique ID of a Closed Freight Exchange. Example: 288.
            closed_freight_exchange_name (str): Name of the Closed Freight Exchange. Example: CFE Acme Group Southern
                Europe.
            mandatory_for_freight_offer (bool): If true, you have to publish your offer in this CFE first, i.e. the
                closedFreightExchangeSetting field is mandatory for
                any freight offer to be submitted. Example: True.
            mandatory_for_vehicle_space_offer (bool): If true, you have to publish your offer in this CFE first, i.e. the
                closedFreightExchangeSetting is mandatory for
                any vehicle space offer to be submitted. Example: True.
            allowed_publication_types (list[ClosedFreightExchangePublicationType]): Allowed publication types for this CFE.
                If the list contains just 'INTERNAL_ONLY' the offers will never be visible outside of the CFE. Example:
                ['INTERNAL_ONLY', 'EXTERNAL_LATER'].
            retention_duration_lower_bound_in_minutes (int | Unset): Lower bound of the retention duration in minutes. This
                is the minimum value to be set for the retention duration in closedFreightExchangeSetting. Example: 5.
            retention_duration_upper_bound_in_minutes (int | Unset): Upper bound of the retention duration in minutes. This
                is the maximum value to be set for the retention duration in closedFreightExchangeSetting. Example: 50.
            default_retention_duration_in_minutes (int | Unset): Default retention duration in minutes.
                This is the default value to be set for the retention duration in closedFreightExchangeSetting (i.e. filled on
                TIMOCOM side if not provided in closedFreightExchangeSetting). Example: 30.
    """

    closed_freight_exchange_id: int
    closed_freight_exchange_name: str
    mandatory_for_freight_offer: bool
    mandatory_for_vehicle_space_offer: bool
    allowed_publication_types: list[ClosedFreightExchangePublicationType]
    retention_duration_lower_bound_in_minutes: int | Unset = UNSET
    retention_duration_upper_bound_in_minutes: int | Unset = UNSET
    default_retention_duration_in_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closed_freight_exchange_id = self.closed_freight_exchange_id

        closed_freight_exchange_name = self.closed_freight_exchange_name

        mandatory_for_freight_offer = self.mandatory_for_freight_offer

        mandatory_for_vehicle_space_offer = self.mandatory_for_vehicle_space_offer

        allowed_publication_types = []
        for allowed_publication_types_item_data in self.allowed_publication_types:
            allowed_publication_types_item = allowed_publication_types_item_data.value
            allowed_publication_types.append(allowed_publication_types_item)

        retention_duration_lower_bound_in_minutes = self.retention_duration_lower_bound_in_minutes

        retention_duration_upper_bound_in_minutes = self.retention_duration_upper_bound_in_minutes

        default_retention_duration_in_minutes = self.default_retention_duration_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "closedFreightExchangeId": closed_freight_exchange_id,
                "closedFreightExchangeName": closed_freight_exchange_name,
                "mandatoryForFreightOffer": mandatory_for_freight_offer,
                "mandatoryForVehicleSpaceOffer": mandatory_for_vehicle_space_offer,
                "allowedPublicationTypes": allowed_publication_types,
            }
        )
        if retention_duration_lower_bound_in_minutes is not UNSET:
            field_dict["retentionDurationLowerBoundInMinutes"] = retention_duration_lower_bound_in_minutes
        if retention_duration_upper_bound_in_minutes is not UNSET:
            field_dict["retentionDurationUpperBoundInMinutes"] = retention_duration_upper_bound_in_minutes
        if default_retention_duration_in_minutes is not UNSET:
            field_dict["defaultRetentionDurationInMinutes"] = default_retention_duration_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        closed_freight_exchange_id = d.pop("closedFreightExchangeId")

        closed_freight_exchange_name = d.pop("closedFreightExchangeName")

        mandatory_for_freight_offer = d.pop("mandatoryForFreightOffer")

        mandatory_for_vehicle_space_offer = d.pop("mandatoryForVehicleSpaceOffer")

        allowed_publication_types = []
        _allowed_publication_types = d.pop("allowedPublicationTypes")
        for allowed_publication_types_item_data in _allowed_publication_types:
            allowed_publication_types_item = ClosedFreightExchangePublicationType(allowed_publication_types_item_data)

            allowed_publication_types.append(allowed_publication_types_item)

        retention_duration_lower_bound_in_minutes = d.pop("retentionDurationLowerBoundInMinutes", UNSET)

        retention_duration_upper_bound_in_minutes = d.pop("retentionDurationUpperBoundInMinutes", UNSET)

        default_retention_duration_in_minutes = d.pop("defaultRetentionDurationInMinutes", UNSET)

        closed_freight_exchange = cls(
            closed_freight_exchange_id=closed_freight_exchange_id,
            closed_freight_exchange_name=closed_freight_exchange_name,
            mandatory_for_freight_offer=mandatory_for_freight_offer,
            mandatory_for_vehicle_space_offer=mandatory_for_vehicle_space_offer,
            allowed_publication_types=allowed_publication_types,
            retention_duration_lower_bound_in_minutes=retention_duration_lower_bound_in_minutes,
            retention_duration_upper_bound_in_minutes=retention_duration_upper_bound_in_minutes,
            default_retention_duration_in_minutes=default_retention_duration_in_minutes,
        )

        closed_freight_exchange.additional_properties = d
        return closed_freight_exchange

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
