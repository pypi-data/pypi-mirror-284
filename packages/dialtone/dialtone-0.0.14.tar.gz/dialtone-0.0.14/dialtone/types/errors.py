import httpx
from enum import Enum
from typing import Any, Dict, Optional


class DialtoneError(Exception):
    pass


class APIError(DialtoneError):
    request: httpx.Request
    message: str
    provider_response: Optional[Dict[str, Any]] = None

    def __str__(self):
        if self.provider_response:
            return f"{self.message} - Provider Response: {self.provider_response}"
        return self.message


class ErrorCode(Enum):
    # Standard
    bad_request = "bad_request"
    unauthorized = "unauthorized"
    not_found = "not_found"
    unprocessable_entity = "unprocessable_entity"
    too_many_requests = "too_many_requests"
    internal_server_error = "internal_server_error"
    # Custom
    provider_moderation = "provider_moderation"
    configuration_error = "configuration_error"


class StatusCode(Enum):
    bad_request = 400
    unauthorized = 401
    not_found = 404
    unprocessable_entity = 422
    too_many_requests = 429
    internal_server_error = 500


class APIStatusError(APIError):
    response: httpx.Response
    status_code: StatusCode

    def __init__(
        self,
        request: httpx.Request,
        response: httpx.Response,
        status_code: StatusCode | None = None,
        message: str | None = None,
        provider_response: Dict[str, Any] | None = None,
    ):
        self.request = request
        self.response = response
        if status_code:
            self.status_code = status_code
        if message:
            self.message = message
        if provider_response:
            self.provider_response = provider_response


class BadRequestError(APIStatusError):
    status_code: StatusCode = StatusCode.bad_request
    message: str = "Bad Request"


class AuthenticationError(APIStatusError):
    status_code: StatusCode = StatusCode.unauthorized
    message: str = "Unauthorized"


class NotFoundError(APIStatusError):
    status_code: StatusCode = StatusCode.not_found
    message: str = "Not Found"


class UnprocessableEntityError(APIStatusError):
    status_code: StatusCode = StatusCode.unprocessable_entity
    message: str = "Unprocessable Entity"


class RateLimitError(APIStatusError):
    status_code: StatusCode = StatusCode.too_many_requests
    message: str = "Too Many Requests"


class InternalServerError(APIStatusError):
    status_code: StatusCode = StatusCode.internal_server_error
    message: str = "Internal Server Error"


class ProviderModerationError(APIError):
    message: str = "Provider Moderation Error"


class ConfigurationError(APIError):
    message: str = "Configuration Error"


class APIConnectionError(APIError):
    message: str = "API Connection Error"

    def __init__(self, request: httpx.Request):
        self.request = request


class APITimeoutError(APIConnectionError):
    message: str = "Request Timeout"
