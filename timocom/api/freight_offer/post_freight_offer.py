from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_resource_response import CreateResourceResponse
from ...models.freight_offer import FreightOffer
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FreightOffer | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/my-freight-offers",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateResourceResponse | Problem | None:
    if response.status_code == 201:
        response_201 = CreateResourceResponse.from_dict(response.json())

        return response_201

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
) -> Response[CreateResourceResponse | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: FreightOffer | Unset = UNSET,
) -> Response[CreateResourceResponse | Problem]:
    """Publish Freight Offer

     Post new Freight Offer.

    Args:
        body (FreightOffer | Unset): A freight offer that is published within the freight exchange
            indicates a demand for transportation. It contains information related to the goods to be
            transported. distance_km field is set in result of a search request, only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResourceResponse | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: FreightOffer | Unset = UNSET,
) -> CreateResourceResponse | Problem | None:
    """Publish Freight Offer

     Post new Freight Offer.

    Args:
        body (FreightOffer | Unset): A freight offer that is published within the freight exchange
            indicates a demand for transportation. It contains information related to the goods to be
            transported. distance_km field is set in result of a search request, only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResourceResponse | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FreightOffer | Unset = UNSET,
) -> Response[CreateResourceResponse | Problem]:
    """Publish Freight Offer

     Post new Freight Offer.

    Args:
        body (FreightOffer | Unset): A freight offer that is published within the freight exchange
            indicates a demand for transportation. It contains information related to the goods to be
            transported. distance_km field is set in result of a search request, only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResourceResponse | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FreightOffer | Unset = UNSET,
) -> CreateResourceResponse | Problem | None:
    """Publish Freight Offer

     Post new Freight Offer.

    Args:
        body (FreightOffer | Unset): A freight offer that is published within the freight exchange
            indicates a demand for transportation. It contains information related to the goods to be
            transported. distance_km field is set in result of a search request, only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResourceResponse | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
