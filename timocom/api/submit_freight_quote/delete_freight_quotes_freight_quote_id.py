from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.freight_exchange_response import FreightExchangeResponse
from ...types import UNSET, Response


def _get_kwargs(
    freight_quote_id: str,
    *,
    timocom_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["timocom_id"] = timocom_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/freight-quotes/{freight_quote_id}".format(
            freight_quote_id=quote(str(freight_quote_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FreightExchangeResponse | None:
    if response.status_code == 204:
        response_204 = FreightExchangeResponse.from_dict(response.json())

        return response_204

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FreightExchangeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    freight_quote_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> Response[FreightExchangeResponse]:
    """Withdraw Freight Quote

     Withdraw a freight quote

    Args:
        freight_quote_id (str): Alphanumeric unique ID which is used to identify an entity
            (freight offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be
            generated on TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FreightExchangeResponse]
    """

    kwargs = _get_kwargs(
        freight_quote_id=freight_quote_id,
        timocom_id=timocom_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    freight_quote_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> FreightExchangeResponse | None:
    """Withdraw Freight Quote

     Withdraw a freight quote

    Args:
        freight_quote_id (str): Alphanumeric unique ID which is used to identify an entity
            (freight offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be
            generated on TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FreightExchangeResponse
    """

    return sync_detailed(
        freight_quote_id=freight_quote_id,
        client=client,
        timocom_id=timocom_id,
    ).parsed


async def asyncio_detailed(
    freight_quote_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> Response[FreightExchangeResponse]:
    """Withdraw Freight Quote

     Withdraw a freight quote

    Args:
        freight_quote_id (str): Alphanumeric unique ID which is used to identify an entity
            (freight offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be
            generated on TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FreightExchangeResponse]
    """

    kwargs = _get_kwargs(
        freight_quote_id=freight_quote_id,
        timocom_id=timocom_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    freight_quote_id: str,
    *,
    client: AuthenticatedClient,
    timocom_id: int,
) -> FreightExchangeResponse | None:
    """Withdraw Freight Quote

     Withdraw a freight quote

    Args:
        freight_quote_id (str): Alphanumeric unique ID which is used to identify an entity
            (freight offer, vehicle space offer, freight quote) in the TIMOCOM system. Will be
            generated on TIMOCOM side, only. Example: NdKoYeUDQheRB14EeyJzTg.
        timocom_id (int): Unique ID of a customer on TIMOCOM side. Example: 288.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FreightExchangeResponse
    """

    return (
        await asyncio_detailed(
            freight_quote_id=freight_quote_id,
            client=client,
            timocom_id=timocom_id,
        )
    ).parsed
