from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClosedFreightExchangePolicyForOfferSearch")


@_attrs_define
class ClosedFreightExchangePolicyForOfferSearch:
    """
    Attributes:
        closed_freight_exchange_id (int): Unique ID of a Closed Freight Exchange. Example: 288.
        closed_freight_exchange_name (str): Name of the Closed Freight Exchange. Example: CFE 1.
    """

    closed_freight_exchange_id: int
    closed_freight_exchange_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closed_freight_exchange_id = self.closed_freight_exchange_id

        closed_freight_exchange_name = self.closed_freight_exchange_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "closedFreightExchangeId": closed_freight_exchange_id,
                "closedFreightExchangeName": closed_freight_exchange_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        closed_freight_exchange_id = d.pop("closedFreightExchangeId")

        closed_freight_exchange_name = d.pop("closedFreightExchangeName")

        closed_freight_exchange_policy_for_offer_search = cls(
            closed_freight_exchange_id=closed_freight_exchange_id,
            closed_freight_exchange_name=closed_freight_exchange_name,
        )

        closed_freight_exchange_policy_for_offer_search.additional_properties = d
        return closed_freight_exchange_policy_for_offer_search

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
