from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.vehicle_space_offers_response import VehicleSpaceOffersResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    ids: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = ids

    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vehicle-space-offers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | VehicleSpaceOffersResponse | None:
    if response.status_code == 200:
        response_200 = VehicleSpaceOffersResponse.from_dict(response.json())

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
) -> Response[Problem | VehicleSpaceOffersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str],
) -> Response[Problem | VehicleSpaceOffersResponse]:
    """Lookup Vehicle Space Offers

     Get a list of Vehicle Space Offers by a list of Ids

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VehicleSpaceOffersResponse]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: list[str],
) -> Problem | VehicleSpaceOffersResponse | None:
    """Lookup Vehicle Space Offers

     Get a list of Vehicle Space Offers by a list of Ids

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VehicleSpaceOffersResponse
    """

    return sync_detailed(
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[str],
) -> Response[Problem | VehicleSpaceOffersResponse]:
    """Lookup Vehicle Space Offers

     Get a list of Vehicle Space Offers by a list of Ids

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VehicleSpaceOffersResponse]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[str],
) -> Problem | VehicleSpaceOffersResponse | None:
    """Lookup Vehicle Space Offers

     Get a list of Vehicle Space Offers by a list of Ids

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VehicleSpaceOffersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
        )
    ).parsed
