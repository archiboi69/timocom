from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_interval import DateInterval
    from ..models.discriminator_aware import DiscriminatorAware
    from ..models.individual_dates import IndividualDates
    from ..models.metre_range import MetreRange
    from ..models.postal_code_areas_array import PostalCodeAreasArray
    from ..models.sorting_step import SortingStep
    from ..models.ton_range import TonRange
    from ..models.vehicle_properties import VehicleProperties


T = TypeVar("T", bound="OfferSearchFilter")


@_attrs_define
class OfferSearchFilter:
    """Is used to search for any offer (freight or vehicle space) in the TIMOCOM Marketplace.

    Attributes:
        inclusive_right_upper_bound_date_time (datetime.datetime): inclusive (<=) right upper bound of creation
            date time.
            Detail:
            In particular if
            exclusiveLeftLowerBoundDateTime is
            set, too, this field is the
            inclusive right upper bound of a
            search interval in matters
            of the update timestamp.
            Timestamp of the first (of possibly multiple)
            request(s) with these filter
            parameters, necessary for
            proper pagination. I.e. if you want to have consistent
            data for multiple pagination requests you should keep
            this value (along with the lower bound) fix.
            A value more than 8 hours in the
            past will be rejected (status
            UNPROCESSABLE_ENTITY)
            and the response will
            contain a message key
            INVALID_QUERY_DATE_TIME of message level
            ERROR. A value in the
            future is set to current
            timestamp on server side. Example: 2019-08-24T14:20:22Z.
        start_location (DiscriminatorAware | PostalCodeAreasArray): Filter parameter for areas/countries. One and only
            one choice elements must be set.
        destination_location (DiscriminatorAware | PostalCodeAreasArray): Filter parameter for areas/countries. One and
            only one choice elements must be set.
        first_result (int): Pagination: Sets the offset position in the result set to start pagination, starting with 0.
            firstResult = (pageNumber-1) * maxResults.
             Default: 0.
        max_results (int): Pagination: Maximum number of returned element of result set. Value is additionally bounded
            above (currently to 30) on server side. Default: 30. Example: 20.
        sortings (list[SortingStep] | Unset): Sorting order of the result list.
        exclusive_left_lower_bound_date_time (datetime.datetime | Unset): exclusive (>) lower bound for creation date
            time. Example: 2019-08-24T14:15:22Z.
        loading_date (DateInterval | IndividualDates | Unset): Either...or choice of date sub filter model
        length_range_m (MetreRange | Unset): Filter criteria that can be defined to find offers which length is within
            the defined range.
        weight_range_t (TonRange | Unset): Filter criteria that can be defined to find offers which weight is within the
            defined range.
        vehicle_properties (VehicleProperties | Unset): Generic type used to describe the properties of a certain
            vehicle with its values.
    """

    inclusive_right_upper_bound_date_time: datetime.datetime
    start_location: DiscriminatorAware | PostalCodeAreasArray
    destination_location: DiscriminatorAware | PostalCodeAreasArray
    first_result: int = 0
    max_results: int = 30
    sortings: list[SortingStep] | Unset = UNSET
    exclusive_left_lower_bound_date_time: datetime.datetime | Unset = UNSET
    loading_date: DateInterval | IndividualDates | Unset = UNSET
    length_range_m: MetreRange | Unset = UNSET
    weight_range_t: TonRange | Unset = UNSET
    vehicle_properties: VehicleProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.date_interval import DateInterval
        from ..models.discriminator_aware import DiscriminatorAware

        inclusive_right_upper_bound_date_time = self.inclusive_right_upper_bound_date_time.isoformat()

        start_location: dict[str, Any]
        if isinstance(self.start_location, DiscriminatorAware):
            start_location = self.start_location.to_dict()
        else:
            start_location = self.start_location.to_dict()

        destination_location: dict[str, Any]
        if isinstance(self.destination_location, DiscriminatorAware):
            destination_location = self.destination_location.to_dict()
        else:
            destination_location = self.destination_location.to_dict()

        first_result = self.first_result

        max_results = self.max_results

        sortings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sortings, Unset):
            sortings = []
            for sortings_item_data in self.sortings:
                sortings_item = sortings_item_data.to_dict()
                sortings.append(sortings_item)

        exclusive_left_lower_bound_date_time: str | Unset = UNSET
        if not isinstance(self.exclusive_left_lower_bound_date_time, Unset):
            exclusive_left_lower_bound_date_time = self.exclusive_left_lower_bound_date_time.isoformat()

        loading_date: dict[str, Any] | Unset
        if isinstance(self.loading_date, Unset):
            loading_date = UNSET
        elif isinstance(self.loading_date, DateInterval):
            loading_date = self.loading_date.to_dict()
        else:
            loading_date = self.loading_date.to_dict()

        length_range_m: dict[str, Any] | Unset = UNSET
        if not isinstance(self.length_range_m, Unset):
            length_range_m = self.length_range_m.to_dict()

        weight_range_t: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight_range_t, Unset):
            weight_range_t = self.weight_range_t.to_dict()

        vehicle_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vehicle_properties, Unset):
            vehicle_properties = self.vehicle_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inclusiveRightUpperBoundDateTime": inclusive_right_upper_bound_date_time,
                "startLocation": start_location,
                "destinationLocation": destination_location,
                "firstResult": first_result,
                "maxResults": max_results,
            }
        )
        if sortings is not UNSET:
            field_dict["sortings"] = sortings
        if exclusive_left_lower_bound_date_time is not UNSET:
            field_dict["exclusiveLeftLowerBoundDateTime"] = exclusive_left_lower_bound_date_time
        if loading_date is not UNSET:
            field_dict["loadingDate"] = loading_date
        if length_range_m is not UNSET:
            field_dict["lengthRange_m"] = length_range_m
        if weight_range_t is not UNSET:
            field_dict["weightRange_t"] = weight_range_t
        if vehicle_properties is not UNSET:
            field_dict["vehicleProperties"] = vehicle_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_interval import DateInterval
        from ..models.discriminator_aware import DiscriminatorAware
        from ..models.individual_dates import IndividualDates
        from ..models.metre_range import MetreRange
        from ..models.postal_code_areas_array import PostalCodeAreasArray
        from ..models.sorting_step import SortingStep
        from ..models.ton_range import TonRange
        from ..models.vehicle_properties import VehicleProperties

        d = dict(src_dict)
        inclusive_right_upper_bound_date_time = isoparse(d.pop("inclusiveRightUpperBoundDateTime"))

        def _parse_start_location(data: object) -> DiscriminatorAware | PostalCodeAreasArray:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemaslocation_search_type_0 = DiscriminatorAware.from_dict(data)

                return componentsschemaslocation_search_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemaslocation_search_type_1 = PostalCodeAreasArray.from_dict(data)

            return componentsschemaslocation_search_type_1

        start_location = _parse_start_location(d.pop("startLocation"))

        def _parse_destination_location(data: object) -> DiscriminatorAware | PostalCodeAreasArray:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemaslocation_search_type_0 = DiscriminatorAware.from_dict(data)

                return componentsschemaslocation_search_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemaslocation_search_type_1 = PostalCodeAreasArray.from_dict(data)

            return componentsschemaslocation_search_type_1

        destination_location = _parse_destination_location(d.pop("destinationLocation"))

        first_result = d.pop("firstResult")

        max_results = d.pop("maxResults")

        _sortings = d.pop("sortings", UNSET)
        sortings: list[SortingStep] | Unset = UNSET
        if _sortings is not UNSET:
            sortings = []
            for sortings_item_data in _sortings:
                sortings_item = SortingStep.from_dict(sortings_item_data)

                sortings.append(sortings_item)

        _exclusive_left_lower_bound_date_time = d.pop("exclusiveLeftLowerBoundDateTime", UNSET)
        exclusive_left_lower_bound_date_time: datetime.datetime | Unset
        if isinstance(_exclusive_left_lower_bound_date_time, Unset):
            exclusive_left_lower_bound_date_time = UNSET
        else:
            exclusive_left_lower_bound_date_time = isoparse(_exclusive_left_lower_bound_date_time)

        def _parse_loading_date(data: object) -> DateInterval | IndividualDates | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasoffer_date_search_choice_type_0 = DateInterval.from_dict(data)

                return componentsschemasoffer_date_search_choice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasoffer_date_search_choice_type_1 = IndividualDates.from_dict(data)

            return componentsschemasoffer_date_search_choice_type_1

        loading_date = _parse_loading_date(d.pop("loadingDate", UNSET))

        _length_range_m = d.pop("lengthRange_m", UNSET)
        length_range_m: MetreRange | Unset
        if isinstance(_length_range_m, Unset):
            length_range_m = UNSET
        else:
            length_range_m = MetreRange.from_dict(_length_range_m)

        _weight_range_t = d.pop("weightRange_t", UNSET)
        weight_range_t: TonRange | Unset
        if isinstance(_weight_range_t, Unset):
            weight_range_t = UNSET
        else:
            weight_range_t = TonRange.from_dict(_weight_range_t)

        _vehicle_properties = d.pop("vehicleProperties", UNSET)
        vehicle_properties: VehicleProperties | Unset
        if isinstance(_vehicle_properties, Unset):
            vehicle_properties = UNSET
        else:
            vehicle_properties = VehicleProperties.from_dict(_vehicle_properties)

        offer_search_filter = cls(
            inclusive_right_upper_bound_date_time=inclusive_right_upper_bound_date_time,
            start_location=start_location,
            destination_location=destination_location,
            first_result=first_result,
            max_results=max_results,
            sortings=sortings,
            exclusive_left_lower_bound_date_time=exclusive_left_lower_bound_date_time,
            loading_date=loading_date,
            length_range_m=length_range_m,
            weight_range_t=weight_range_t,
            vehicle_properties=vehicle_properties,
        )

        offer_search_filter.additional_properties = d
        return offer_search_filter

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
