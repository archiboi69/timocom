from __future__ import annotations

import json
from typing import Any

import httpx
import structlog
from structlog.contextvars import bound_contextvars, get_contextvars

_RAW_PREVIEW_MAX_LEN = 1200


def bind_observability_context(**fields: Any):
    return bound_contextvars(**fields)


def current_observability_context() -> dict[str, Any]:
    return dict(get_contextvars())


def log_sdk_event(
    logger_name: str,
    *,
    operation: str,
    method: str,
    url: str,
    duration_ms: float,
    status_code: int | None = None,
    provider_request_id: str | None = None,
    request_body: Any = None,
    response_body: Any = None,
    response_headers: dict[str, Any] | None = None,
    error: dict[str, Any] | None = None,
    **extra: Any,
) -> None:
    event: dict[str, Any] = {
        "kind": "sdk_event",
        "sdk": "timocom",
        "operation": operation,
        "method": method,
        "url": url,
        "duration_ms": round(duration_ms, 1),
        **current_observability_context(),
        **extra,
    }
    if status_code is not None:
        event["status_code"] = status_code
    if provider_request_id is not None:
        event["provider_request_id"] = provider_request_id
    if request_body is not None:
        event["request_body"] = request_body
    if response_body is not None:
        event["response_body"] = response_body
    if response_headers is not None:
        event["response_headers"] = response_headers
    if error is not None:
        event["error"] = error

    logger = structlog.get_logger(logger_name)
    if error is not None or (status_code is not None and status_code >= 400):
        logger.error("sdk_event", **event)
        return
    logger.info("sdk_event", **event)


def request_operation(method: str, url: str) -> str:
    path = httpx.URL(url).path.strip("/") or "root"
    return f"{method.lower()}_{path.replace('/', '_').replace('-', '_')}"


def redact_headers(headers: dict[str, Any]) -> dict[str, Any]:
    safe_headers: dict[str, Any] = {}
    for key, value in headers.items():
        if key.lower() in {"authorization", "cookie", "set-cookie"}:
            safe_headers[key] = "[REDACTED]"
            continue
        safe_headers[key] = value
    return safe_headers


def serialize_request_content(content: Any) -> Any:
    if content in (None, b"", ""):
        return None
    if isinstance(content, bytes):
        text = content.decode("utf-8", errors="replace")
    else:
        text = str(content)
    return _compact_text(text)


def serialize_response_body(resp: httpx.Response) -> Any:
    try:
        payload = resp.json()
    except json.JSONDecodeError:
        text = resp.text or ""
        if not text:
            return None
        return _compact_text(text)
    if isinstance(payload, dict):
        return _redact_json(payload)
    if isinstance(payload, list):
        return [_redact_json(item) if isinstance(item, dict) else item for item in payload]
    return payload


def provider_request_id(resp: httpx.Response) -> str | None:
    for key in ("x-request-id", "request-id", "x-correlation-id"):
        value = resp.headers.get(key)
        if value:
            return value
    return None


def _redact_json(value: dict[str, Any]) -> dict[str, Any]:
    safe: dict[str, Any] = {}
    for key, item in value.items():
        if any(secret in key.lower() for secret in ("token", "password", "authorization")):
            safe[key] = "[REDACTED]"
            continue
        safe[key] = item
    return safe


def _compact_text(value: str) -> str:
    return " ".join(value.split())[:_RAW_PREVIEW_MAX_LEN]
