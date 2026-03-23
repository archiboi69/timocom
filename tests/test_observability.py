from __future__ import annotations

import httpx
from structlog.testing import capture_logs

from timocom import AuthenticatedClient, bind_observability_context
from timocom.api.enumeration import get_currencies


def test_client_request_logs_transport_event() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={"enumerations": []},
            headers={"x-request-id": "tc-req-1"},
            request=request,
        )

    raw_client = httpx.Client(
        base_url="https://api.timocom.test",
        transport=httpx.MockTransport(handler),
    )
    client = AuthenticatedClient(
        base_url="https://api.timocom.test",
        token="secret-token",
        prefix="Basic",
    ).set_httpx_client(raw_client)

    with capture_logs() as logs:
        with bind_observability_context(request_id="req-123", operation_id="op-456"):
            response = get_currencies.sync_detailed(client=client, timocom_id=288)

    assert response.status_code == 200
    assert logs[0]["kind"] == "sdk_event"
    assert logs[0]["sdk"] == "timocom"
    assert logs[0]["request_id"] == "req-123"
    assert logs[0]["operation_id"] == "op-456"
    assert logs[0]["provider_request_id"] == "tc-req-1"
    assert logs[0]["status_code"] == 200
    assert logs[0]["method"] == "get"
    assert logs[0]["url"].endswith("/enumerations/currencies?timocom_id=288")


def test_client_request_logs_transport_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("timocom down", request=request)

    raw_client = httpx.Client(
        base_url="https://api.timocom.test",
        transport=httpx.MockTransport(handler),
    )
    client = AuthenticatedClient(
        base_url="https://api.timocom.test",
        token="secret-token",
        prefix="Basic",
    ).set_httpx_client(raw_client)

    with capture_logs() as logs:
        try:
            get_currencies.sync_detailed(client=client, timocom_id=288)
        except httpx.ConnectError:
            pass
        else:
            raise AssertionError("expected ConnectError")

    assert logs[0]["kind"] == "sdk_event"
    assert logs[0]["sdk"] == "timocom"
    assert logs[0]["error"]["type"] == "ConnectError"
    assert logs[0]["error"]["retryable"] is True
