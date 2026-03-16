from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.closed_freight_exchange_publication_type import ClosedFreightExchangePublicationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClosedFreightExchangeSetting")


@_attrs_define
class ClosedFreightExchangeSetting:
    """The Closed Freight Exchange (briefly CFE, or in German: Geschlossene Frachtenbörse) is a concept of grouping TIMOCOM
    customers for offer publication constraints purposes. The common use case is that an offer with CFE settings will be
    published exclusively within the CFE in the first place. This means that it is not visible to any TIMOCOM customer
    which is not member of the set CFE. After a set duration of time (maybe never) it will be automatically visible to
    all TIMOCOM customers unless it has not been withdrawn before.

    If your company has a valid CFE contract with TIMOCOM you are able to send via the API all Closed Freight Exchange
    settings with the submitted offer.

        Attributes:
            closed_freight_exchange_id (int): Unique ID of a Closed Freight Exchange. Example: 288.
            publication_type (ClosedFreightExchangePublicationType): Publication type: Visible within, only or publish
                outside of the CFE after expired retention time. Example: EXTERNAL_LATER.
            publication_date_time (datetime.datetime | Unset): At this calculated timestamp the offer will be
                published outside of the CFE. Not to be set on client side.
                 Example: 2019-08-24T14:15:22Z.
            remark (str | Unset): Remark visible to members of this Closed Freight Exchange, only. Example: External Remark.
            retention_duration_in_minutes (int | Unset): Retention time for remaining in CFE, visible for CFE members, only
                Example: 5.
    """

    closed_freight_exchange_id: int
    publication_type: ClosedFreightExchangePublicationType
    publication_date_time: datetime.datetime | Unset = UNSET
    remark: str | Unset = UNSET
    retention_duration_in_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        closed_freight_exchange_id = self.closed_freight_exchange_id

        publication_type = self.publication_type.value

        publication_date_time: str | Unset = UNSET
        if not isinstance(self.publication_date_time, Unset):
            publication_date_time = self.publication_date_time.isoformat()

        remark = self.remark

        retention_duration_in_minutes = self.retention_duration_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "closedFreightExchangeId": closed_freight_exchange_id,
                "publicationType": publication_type,
            }
        )
        if publication_date_time is not UNSET:
            field_dict["publicationDateTime"] = publication_date_time
        if remark is not UNSET:
            field_dict["remark"] = remark
        if retention_duration_in_minutes is not UNSET:
            field_dict["retentionDurationInMinutes"] = retention_duration_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        closed_freight_exchange_id = d.pop("closedFreightExchangeId")

        publication_type = ClosedFreightExchangePublicationType(d.pop("publicationType"))

        _publication_date_time = d.pop("publicationDateTime", UNSET)
        publication_date_time: datetime.datetime | Unset
        if isinstance(_publication_date_time, Unset):
            publication_date_time = UNSET
        else:
            publication_date_time = isoparse(_publication_date_time)

        remark = d.pop("remark", UNSET)

        retention_duration_in_minutes = d.pop("retentionDurationInMinutes", UNSET)

        closed_freight_exchange_setting = cls(
            closed_freight_exchange_id=closed_freight_exchange_id,
            publication_type=publication_type,
            publication_date_time=publication_date_time,
            remark=remark,
            retention_duration_in_minutes=retention_duration_in_minutes,
        )

        closed_freight_exchange_setting.additional_properties = d
        return closed_freight_exchange_setting

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
