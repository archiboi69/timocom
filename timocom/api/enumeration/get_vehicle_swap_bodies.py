from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enumeration_response import EnumerationResponse
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
        "url": "/enumerations/vehicle-properties/vehicle-swap-bodies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnumerationResponse | Problem | None:
    if response.status_code == 200:
        response_200 = EnumerationResponse.from_dict(response.json())

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
) -> Response[EnumerationResponse | Problem]:
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
) -> Response[EnumerationResponse | Problem]:
    """Get vehicle swap bodies

     Get a list of all vehicle swap bodies.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnumerationResponse | Problem]
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
) -> EnumerationResponse | Problem | None:
    """Get vehicle swap bodies

     Get a list of all vehicle swap bodies.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnumerationResponse | Problem
    """

    return sync_detailed(
        client=client,
        timocom_id=timocom_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> Response[EnumerationResponse | Problem]:
    """Get vehicle swap bodies

     Get a list of all vehicle swap bodies.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnumerationResponse | Problem]
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
) -> EnumerationResponse | Problem | None:
    """Get vehicle swap bodies

     Get a list of all vehicle swap bodies.

    Args:
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnumerationResponse | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            timocom_id=timocom_id,
        )
    ).parsed
