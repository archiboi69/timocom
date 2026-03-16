from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.freight_quotes_response import FreightQuotesResponse
from ...models.problem import Problem
from ...types import UNSET, Response


def _get_kwargs(
    public_offer_id: str,
    *,
    timocom_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["timocom_id"] = timocom_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/my-freight-offers/{public_offer_id}/freight-quotes".format(
            public_offer_id=quote(str(public_offer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FreightQuotesResponse | Problem | None:
    if response.status_code == 200:
        response_200 = FreightQuotesResponse.from_dict(response.json())

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
) -> Response[FreightQuotesResponse | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    public_offer_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> Response[FreightQuotesResponse | Problem]:
    """Get Received Freight Quotes for Your Freight Offer

     Get a list of Freight Quotes by a Freight Offer ID (TIMOCOM’s publicOfferId). The timocom_id (query
    param) must be the TIMOCOM ID of the freight offer referenced by the publicOfferId path param.

    Args:
        public_offer_id (str): Alphanumeric unique ID which is used to identify an entity (freight
            offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be generated on
            TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FreightQuotesResponse | Problem]
    """

    kwargs = _get_kwargs(
        public_offer_id=public_offer_id,
        timocom_id=timocom_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_offer_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> FreightQuotesResponse | Problem | None:
    """Get Received Freight Quotes for Your Freight Offer

     Get a list of Freight Quotes by a Freight Offer ID (TIMOCOM’s publicOfferId). The timocom_id (query
    param) must be the TIMOCOM ID of the freight offer referenced by the publicOfferId path param.

    Args:
        public_offer_id (str): Alphanumeric unique ID which is used to identify an entity (freight
            offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be generated on
            TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FreightQuotesResponse | Problem
    """

    return sync_detailed(
        public_offer_id=public_offer_id,
        client=client,
        timocom_id=timocom_id,
    ).parsed


async def asyncio_detailed(
    public_offer_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> Response[FreightQuotesResponse | Problem]:
    """Get Received Freight Quotes for Your Freight Offer

     Get a list of Freight Quotes by a Freight Offer ID (TIMOCOM’s publicOfferId). The timocom_id (query
    param) must be the TIMOCOM ID of the freight offer referenced by the publicOfferId path param.

    Args:
        public_offer_id (str): Alphanumeric unique ID which is used to identify an entity (freight
            offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be generated on
            TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FreightQuotesResponse | Problem]
    """

    kwargs = _get_kwargs(
        public_offer_id=public_offer_id,
        timocom_id=timocom_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_offer_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> FreightQuotesResponse | Problem | None:
    """Get Received Freight Quotes for Your Freight Offer

     Get a list of Freight Quotes by a Freight Offer ID (TIMOCOM’s publicOfferId). The timocom_id (query
    param) must be the TIMOCOM ID of the freight offer referenced by the publicOfferId path param.

    Args:
        public_offer_id (str): Alphanumeric unique ID which is used to identify an entity (freight
            offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be generated on
            TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FreightQuotesResponse | Problem
    """

    return (
        await asyncio_detailed(
            public_offer_id=public_offer_id,
            client=client,
            timocom_id=timocom_id,
        )
    ).parsed
