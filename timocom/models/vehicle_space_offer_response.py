from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freight_exchange_response_meta import FreightExchangeResponseMeta
    from ..models.vehicle_space_offer import VehicleSpaceOffer


T = TypeVar("T", bound="VehicleSpaceOfferResponse")


@_attrs_define
class VehicleSpaceOfferResponse:
    """
    Attributes:
        meta (FreightExchangeResponseMeta | Unset):
        payload (VehicleSpaceOffer | Unset): A vehicle space offer that is published within the freight exchange
            indicates available vehicle space. It contains information related to available vehicle.

            * The Sum of truckLength_m and trailerLength_m has to be greater than 0.
            * The Sum of truckWeight_t and trailerWeight_t has to be greater than 0.
    """

    meta: FreightExchangeResponseMeta | Unset = UNSET
    payload: VehicleSpaceOffer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freight_exchange_response_meta import FreightExchangeResponseMeta
        from ..models.vehicle_space_offer import VehicleSpaceOffer

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: FreightExchangeResponseMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = FreightExchangeResponseMeta.from_dict(_meta)

        _payload = d.pop("payload", UNSET)
        payload: VehicleSpaceOffer | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = VehicleSpaceOffer.from_dict(_payload)

        vehicle_space_offer_response = cls(
            meta=meta,
            payload=payload,
        )

        vehicle_space_offer_response.additional_properties = d
        return vehicle_space_offer_response

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
