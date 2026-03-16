from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.closed_freight_exchange_policy_for_offer_publisher_response_upcoming import (
    ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming,
)
from ...models.problem import Problem
from ...types import UNSET, Response


def _get_kwargs(
    *,
    timocom_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["timocom_id"] = timocom_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/closed-freight-exchange-policy/publisher",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem | None:
    if response.status_code == 200:
        response_200 = ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> Response[ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem]:
    """Get Closed Freight Exchange Policies (Offer Publishing)

     Get a list of all Closed Freight Exchange Policies for Offer Publishing.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem]
    """

    kwargs = _get_kwargs(
        timocom_id=timocom_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem | None:
    """Get Closed Freight Exchange Policies (Offer Publishing)

     Get a list of all Closed Freight Exchange Policies for Offer Publishing.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem
    """

    return sync_detailed(
        client=client,
        timocom_id=timocom_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> Response[ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem]:
    """Get Closed Freight Exchange Policies (Offer Publishing)

     Get a list of all Closed Freight Exchange Policies for Offer Publishing.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem]
    """

    kwargs = _get_kwargs(
        timocom_id=timocom_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem | None:
    """Get Closed Freight Exchange Policies (Offer Publishing)

     Get a list of all Closed Freight Exchange Policies for Offer Publishing.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClosedFreightExchangePolicyForOfferPublisherResponseUpcoming | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            timocom_id=timocom_id,
        )
    ).parsed
