from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.start_ad_hoc_query_request_data import StartAdHocQueryRequestData
from ...models.start_ad_hoc_query_response import StartAdHocQueryResponse
from typing import Dict



def _get_kwargs(
    *,
    body: StartAdHocQueryRequestData,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/start_query",
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[StartAdHocQueryResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StartAdHocQueryResponse.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[StartAdHocQueryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StartAdHocQueryRequestData,

) -> Response[StartAdHocQueryResponse]:
    """ Start a new non-blocking ad-hoc query.

     Start a new non-blocking ad-hoc query.

    Query progress can be checked at `/v1/query_progress/{qr_id}`.

    Args:
        body (StartAdHocQueryRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartAdHocQueryResponse]
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
    body: StartAdHocQueryRequestData,

) -> Optional[StartAdHocQueryResponse]:
    """ Start a new non-blocking ad-hoc query.

     Start a new non-blocking ad-hoc query.

    Query progress can be checked at `/v1/query_progress/{qr_id}`.

    Args:
        body (StartAdHocQueryRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartAdHocQueryResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StartAdHocQueryRequestData,

) -> Response[StartAdHocQueryResponse]:
    """ Start a new non-blocking ad-hoc query.

     Start a new non-blocking ad-hoc query.

    Query progress can be checked at `/v1/query_progress/{qr_id}`.

    Args:
        body (StartAdHocQueryRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartAdHocQueryResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: StartAdHocQueryRequestData,

) -> Optional[StartAdHocQueryResponse]:
    """ Start a new non-blocking ad-hoc query.

     Start a new non-blocking ad-hoc query.

    Query progress can be checked at `/v1/query_progress/{qr_id}`.

    Args:
        body (StartAdHocQueryRequestData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartAdHocQueryResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
