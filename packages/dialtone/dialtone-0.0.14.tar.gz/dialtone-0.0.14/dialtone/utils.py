import httpx
from typing import Any, Type
from dialtone.types import (
    BadRequestError,
    AuthenticationError,
    NotFoundError,
    UnprocessableEntityError,
    RateLimitError,
    InternalServerError,
    ProviderModerationError,
    ConfigurationError,
    APIConnectionError,
    APITimeoutError,
    APIError,
    ErrorCode,
    StatusCode,
)
from dialtone.config import DEFAULT_REQUEST_TIMEOUT


def get_error_status_code_from_code(error_code: ErrorCode) -> StatusCode:
    STATUS_CODE_FROM_CODE = {
        ErrorCode.bad_request: StatusCode.bad_request,
        ErrorCode.unauthorized: StatusCode.unauthorized,
        ErrorCode.not_found: StatusCode.not_found,
        ErrorCode.unprocessable_entity: StatusCode.unprocessable_entity,
        ErrorCode.too_many_requests: StatusCode.too_many_requests,
        ErrorCode.internal_server_error: StatusCode.internal_server_error,
    }

    return STATUS_CODE_FROM_CODE[error_code]


def get_error_code_from_status_code(status_code: StatusCode) -> ErrorCode:
    CODE_FROM_STATUS_CODE = {
        StatusCode.bad_request: ErrorCode.bad_request,
        StatusCode.unauthorized: ErrorCode.unauthorized,
        StatusCode.not_found: ErrorCode.not_found,
        StatusCode.unprocessable_entity: ErrorCode.unprocessable_entity,
        StatusCode.too_many_requests: ErrorCode.too_many_requests,
        StatusCode.internal_server_error: ErrorCode.internal_server_error,
    }

    return CODE_FROM_STATUS_CODE[status_code]


def get_error_class_by_status_code(exception: httpx.HTTPStatusError) -> Type[APIError]:
    status_code = StatusCode(exception.response.status_code)

    if status_code == StatusCode.bad_request:
        return BadRequestError
    elif status_code == StatusCode.unauthorized:
        return AuthenticationError
    elif status_code == StatusCode.not_found:
        return NotFoundError
    elif status_code == StatusCode.unprocessable_entity:
        return UnprocessableEntityError
    elif status_code == StatusCode.too_many_requests:
        return RateLimitError
    elif status_code == StatusCode.internal_server_error:
        return InternalServerError
    else:
        raise exception


def get_error_class_by_code(exception: httpx.HTTPStatusError) -> Type[APIError]:
    error_code = ErrorCode(exception.response.json().get("detail").get("error_code"))

    if error_code == ErrorCode.bad_request:
        return BadRequestError
    elif error_code == ErrorCode.unauthorized:
        return AuthenticationError
    elif error_code == ErrorCode.not_found:
        return NotFoundError
    elif error_code == ErrorCode.unprocessable_entity:
        return UnprocessableEntityError
    elif error_code == ErrorCode.too_many_requests:
        return RateLimitError
    elif error_code == ErrorCode.internal_server_error:
        return InternalServerError
    elif error_code == ErrorCode.provider_moderation:
        return ProviderModerationError
    elif error_code == ErrorCode.configuration_error:
        return ConfigurationError
    else:
        raise exception


def process_response(response: httpx.Response):
    try:
        response.raise_for_status()
    except httpx.RequestError as exc:
        if isinstance(exc, httpx.TimeoutException):
            raise APITimeoutError(request=exc.request) from None
        raise APIConnectionError(request=exc.request)
    except httpx.HTTPStatusError as exc:
        error_params = {
            "status_code": StatusCode(exc.response.status_code),
            "request": exc.request,
            "response": exc.response,
        }

        try:
            response_body = exc.response.json()
            error_code = response_body.get("detail", {}).get("error_code")

            if error_code:
                # Happy path
                error_class = get_error_class_by_code(exc)

                if response_body.get("detail").get("message"):
                    error_params["message"] = response_body["detail"]["message"]
                if response_body.get("detail").get("provider_response"):
                    error_params["provider_response"] = response_body["detail"][
                        "provider_response"
                    ]

                raise error_class(**error_params) from None
            else:
                # Response body is JSON but is invalid format
                error_class = get_error_class_by_status_code(exc)
                raise error_class(**error_params) from None
        except httpx.DecodingError:
            # Response body is not valid JSON
            error_class = get_error_class_by_status_code(exc)
            error_params["message"] = exc.response.text
            raise error_class(**error_params) from None

    return response.json()


def dialtone_post_request(
    url: str,
    data: dict[str, Any],
    headers: dict[str, str],
    timeout: int = DEFAULT_REQUEST_TIMEOUT,
) -> dict:
    with httpx.Client() as client:
        response = client.post(url, json=data, headers=headers, timeout=timeout)
        return process_response(response)


async def dialtone_post_request_async(
    url: str,
    data: dict[str, Any],
    headers: dict[str, str],
    timeout: int = DEFAULT_REQUEST_TIMEOUT,
) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers, timeout=timeout)
        return process_response(response)
