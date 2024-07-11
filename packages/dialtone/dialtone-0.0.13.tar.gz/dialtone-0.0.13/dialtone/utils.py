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


def process_response(response: httpx.Response):
    try:
        response.raise_for_status()
    except httpx.RequestError as exc:
        if isinstance(exc, httpx.TimeoutException):
            raise APITimeoutError(request=exc.request) from None
        raise APIConnectionError(request=exc.request)
    except httpx.HTTPStatusError as exc:
        message = None
        error_params = {
            "request": exc.request,
            "response": exc.response,
        }

        try:
            response_body = exc.response.json()
            if response_body.get("detail"):
                message = response_body["detail"]
        except httpx.DecodingError:
            pass

        if message:
            error_params["message"] = message

        if exc.response.status_code == 400:
            raise BadRequestError(**error_params) from None
        elif exc.response.status_code == 401:
            raise AuthenticationError(**error_params) from None
        elif exc.response.status_code == 404:
            raise NotFoundError(**error_params) from None
        elif exc.response.status_code == 422:
            raise UnprocessableEntityError(**error_params) from None
        elif exc.response.status_code == 429:
            raise RateLimitError(**error_params) from None
        elif exc.response.status_code == 500:
            raise InternalServerError(**error_params) from None
        else:
            raise exc

    return response.json()


def dialtone_post_request(
    url: str,
    data: dict[str, Any],
    headers: dict[str, str],
    timeout: int = DEFAULT_HTTP_TIMEOUT,
) -> dict:
    with httpx.Client() as client:
        response = client.post(url, json=data, headers=headers, timeout=timeout)
        return process_response(response)


async def dialtone_post_request_async(
    url: str,
    data: dict[str, Any],
    headers: dict[str, str],
    timeout: int = DEFAULT_HTTP_TIMEOUT,
) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers, timeout=timeout)
        return process_response(response)
