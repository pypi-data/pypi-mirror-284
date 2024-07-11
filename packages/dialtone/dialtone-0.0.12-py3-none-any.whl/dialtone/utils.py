from dialtone.types import (
    BadRequestError,
    AuthenticationError,
    NotFoundError,
    UnprocessableEntityError,
    RateLimitError,
    InternalServerError,
    APIConnectionError,
    APITimeoutError,
)
import httpx
from typing import Any


DEFAULT_HTTP_TIMEOUT = 120


def dialtone_post_request(
    url: str,
    data: dict[str, Any],
    headers: dict[str, str],
    timeout: int = DEFAULT_HTTP_TIMEOUT,
) -> dict:
    try:
        with httpx.Client() as client:
            response = client.post(url, json=data, headers=headers, timeout=timeout)
            response.raise_for_status()
    except httpx.RequestError as exc:
        if isinstance(exc, httpx.TimeoutException):
            raise APITimeoutError(request=exc.request) from exc
        raise APIConnectionError(request=exc.request) from exc
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 400:
            raise BadRequestError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 401:
            raise AuthenticationError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 404:
            raise NotFoundError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 422:
            raise UnprocessableEntityError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 429:
            raise RateLimitError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 500:
            raise InternalServerError(request=exc.request, response=exc.response)
        else:
            raise exc
    return response.json()


async def dialtone_post_request_async(
    url: str,
    data: dict[str, Any],
    headers: dict[str, str],
    timeout: int = DEFAULT_HTTP_TIMEOUT,
) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, json=data, headers=headers, timeout=timeout
            )
            response.raise_for_status()
    except httpx.RequestError as exc:
        if isinstance(exc, httpx.TimeoutException):
            raise APITimeoutError(request=exc.request) from exc
        raise APIConnectionError(request=exc.request) from exc
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 400:
            raise BadRequestError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 401:
            raise AuthenticationError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 404:
            raise NotFoundError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 422:
            raise UnprocessableEntityError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 429:
            raise RateLimitError(request=exc.request, response=exc.response)
        elif exc.response.status_code == 500:
            raise InternalServerError(request=exc.request, response=exc.response)
        else:
            raise exc
    return response.json()
