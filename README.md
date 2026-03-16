# timocom SDK
A Python client library for accessing the TIMOCOM Freight Exchange API.

This SDK is generated automatically from the official TIMOCOM OpenAPI specification. It provides a strongly typed, modern, and reliable interface for interacting with TIMOCOM's live and sandbox environments.

## Installation

Since this is a private repository, you can install it into your project directly using `uv` or `pip` via git.

**Using uv:**
```bash
uv add "git+ssh://git@github.com/archiboi69/timocom.git"
```

**Using pip:**
```bash
pip install git+ssh://git@github.com/archiboi69/timocom.git
```

## Usage
First, create a client:

```python
from timocom import Client

client = Client(base_url="https://sandbox.timocom.com/freight-exchange/3")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead. The TIMOCOM API requires Basic Authentication. You must encode your `username:password` using Base64.

```python
import base64
from timocom import AuthenticatedClient

# 1. Prepare your credentials
credentials = "your_username:your_password"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# 2. Initialize the Authenticated Client
# Use https://sandbox.timocom.com/freight-exchange/3 for testing
# Use https://api.timocom.com/freight-exchange/3 for production
client = AuthenticatedClient(
    base_url="https://api.timocom.com/freight-exchange/3", 
    token=encoded_credentials,
    prefix="Basic" # Required for TIMOCOM API
)
```

Now call your endpoint and use your models:

```python
from timocom.models import FreightOffersResponse
from timocom.api.freight_offer import get_my_freight_offers
from timocom.types import Response

your_timocom_id = 123456

with client as client:
    # Option A: Get the raw parsed model directly
    my_data: FreightOffersResponse = get_my_freight_offers.sync(client=client, timocom_id=your_timocom_id)
    
    # Option B: Get the detailed HTTP response (includes status codes, headers)
    response: Response[FreightOffersResponse] = get_my_freight_offers.sync_detailed(client=client, timocom_id=your_timocom_id)
```

Or do the same thing with an async version:

```python
import asyncio
from timocom.models import FreightOffersResponse
from timocom.api.freight_offer import get_my_freight_offers
from timocom.types import Response

your_timocom_id = 123456

async def fetch_offers():
    async with client as client:
        my_data: FreightOffersResponse = await get_my_freight_offers.asyncio(client=client, timocom_id=your_timocom_id)
        response: Response[FreightOffersResponse] = await get_my_freight_offers.asyncio_detailed(client=client, timocom_id=your_timocom_id)

asyncio.run(fetch_offers())
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://sandbox.timocom.com/freight-exchange/3", 
    token=encoded_credentials,
    prefix="Basic",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://sandbox.timocom.com/freight-exchange/3", 
    token=encoded_credentials,
    prefix="Basic", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (e.g. `freight_offer` above)
1. Any endpoint which did not have a tag will be in `timocom.api.default`

## Advanced customizations & Resilience

This SDK uses `httpx` under the hood. It is highly recommended to wrap your API calls using a retry library like `tenacity` when building agents or robust scripts to handle TIMOCOM's rate limits (429) or transient 5xx server errors.

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from timocom import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://sandbox.timocom.com/freight-exchange/3",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from timocom import Client

client = Client(
    base_url="https://sandbox.timocom.com/freight-exchange/3",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://sandbox.timocom.com/freight-exchange/3", proxies="http://localhost:8030"))
```

## Building / publishing this package
This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies and packaging. Here are the basics:
1. Update the metadata in `pyproject.toml` (e.g. authors, version).
2. If you're using a private repository: https://docs.astral.sh/uv/guides/integration/alternative-indexes/
3. Build a distribution with `uv build`, builds `sdist` and `wheel` by default.
1. Publish the client with `uv publish`, see documentation for publishing to private indexes.

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using uv**, you can simply do `uv add <path-to-this-client>` from that project
1. If that project is not using uv:
    1. Build a wheel with `uv build --wheel`.
    1. Install that wheel from the other project `pip install <path-to-wheel>`.
