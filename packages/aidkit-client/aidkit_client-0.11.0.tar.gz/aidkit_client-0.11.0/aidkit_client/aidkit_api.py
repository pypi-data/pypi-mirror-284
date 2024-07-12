"""
Service class to handle low-level communication.
"""

import asyncio
import functools
import json
import typing
from abc import ABC, abstractmethod
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Callable, Coroutine, Dict, Optional, TypeVar, Union

import httpx
from typing_extensions import ParamSpec

from aidkit_client._endpoints.models import AugmentationErrorType
from aidkit_client.authenticator import AuthenticatorService
from aidkit_client.exceptions import (
    AidkitClientError,
    AugmentationAlgorithmicError,
    AugmentationExecutionError,
    AugmentationNotFoundError,
    AuthenticationError,
    DataDimensionError,
    DataFormatError,
    InvalidParametersError,
    MultipleSubsetsReportAggregationError,
    ResourceWithNameNotFoundError,
    TooManyRequestsError,
)

API_VERSION = "1.0"


class HTTPXTimeoutException(Exception):
    """
    Exception raised if some httpx timeout is raised.
    """


@dataclass
class Response:
    """
    Response of an aidkit server.
    """

    status_code: int
    body: Union[Dict[str, Any], str, bytes]

    @property
    def is_success(self) -> bool:
        """
        Return whether the request prompting the response was handled
        successfully.

        :return: True if the aidkit server indicated success, False otherwise.
        """
        return self.status_code in (200, 201, 204)

    @property
    def is_not_found(self) -> bool:
        """
        Return whether a resource was not found.

        :return: True if the aidkit server indicated that a resource was not
            found, False otherwise.
        """
        return self.status_code == 404

    @property
    def is_bad(self) -> bool:
        """
        Return whether the request prompting the response was deemed a bad
        request by the server.

        :return: True if the server returned a "bad request" error code, False
            otherwise.
        """
        return self.status_code == 400

    @property
    def is_forbidden(self) -> bool:
        """
        Return whether the request prompting the response was deemed a forbidden
        request by the server.

        :return: True if the server returned a "forbidden" error code, False
            otherwise.
        """
        return self.status_code == 403

    @property
    def is_unprocessable(self) -> bool:
        """
        Return whether the request content was deemed unprocessable by the server.

        :return: True if the server returned a "unprocessable content" error code, False
            otherwise.
        """
        return self.status_code == 422

    @staticmethod
    def _is_augmentation_service_response(response: Union[Dict[str, Any], str, bytes]) -> bool:
        return isinstance(response, dict) and "error_type" in response and "description" in response

    def _raise_error_based_on_status_code(self, error_message: str) -> None:
        """
        Raise the appropriate error based on the status code of the response.

        :param error_message: Error message to prepend to the raised error if
            an error is raised. Must contain relevant context.
        :raises AuthenticationError: If the server returned a 401 status code.
        :raises ResourceWithNameNotFoundError: If the server returned a 404
            status code.
        :raises AidkitClientError: If some other error occured or if the server did
            not return a dictionary.
        :raises MultipleSubsetsReportAggregationError: If a report is retrieved for pipeline runs
            using different subsets.
        :raises AugmentationNotFoundError: If an augmentation is requested but not available.
        :raises DataFormatError: If an image file provided is the incorrect format.
        :raises DataDimensionError: If the provided image files are the incorrect size.
        :raises InvalidParametersError: If the provided parameters are incorrect.
        :raises AugmentationAlgorithmicError: A run time error commonly related to mathematical
            operation issue.
        :raises AugmentationExecutionError: The augmentation execution has failed.
        :raises TooManyRequestsError: If the server returned a 429 status code.
        """
        if isinstance(self.body, bytes):
            error_details = f"Server responded with error code {self.status_code}."
        else:
            error_details = (
                f"Server responded with error code {self.status_code}" f" and message {self.body}."
            )

        if self.is_unprocessable and self._is_augmentation_service_response(self.body):
            error_message = self.body["description"]  # type: ignore
            error_type = self.body["error_type"]  # type: ignore

            if error_type == AugmentationErrorType.INVALID_PARAMETERS.value:
                raise InvalidParametersError(error_message)
            if error_type == AugmentationErrorType.DATA_FORMAT.value:
                raise DataFormatError(error_message)
            if error_type == AugmentationErrorType.DATA_DIMENSION.value:
                raise DataDimensionError(error_message)

        if self.status_code == 401:
            if (
                isinstance(self.body, dict)
                and "error" in self.body
                and "detail" in self.body["error"]
                and isinstance(self.body["error"]["detail"], str)
            ):
                if self.body["error"]["detail"].startswith(
                    "AuthApiError('Authorization failed: Unable to find a signing key that matches:"
                ):
                    raise AuthenticationError("JWT token is not usable for this domain.")
                if (
                    self.body["error"]["detail"]
                    == "AuthApiError('Authorization failed: Signature has expired')"
                ):
                    raise AuthenticationError("Used JWT token is expired.")

            if isinstance(self.body, bytes):
                raise AuthenticationError()
            raise AuthenticationError(f"Server response: '{self.body}'")
        if self.status_code == 429:
            raise TooManyRequestsError(
                "The endpoint is handling too many requests. Please retry later."
            )

        if self.is_not_found:
            if self._is_augmentation_service_response(self.body):
                raise AugmentationNotFoundError(self.body["description"])  # type: ignore
            raise ResourceWithNameNotFoundError(
                error_message,
                error_details,
            )
        if self.is_forbidden:
            if (
                isinstance(self.body, dict)
                and "error" in self.body
                and "detail" in self.body["error"]
                and isinstance(self.body["error"]["detail"], str)
            ):
                if self.body["error"]["detail"].startswith(
                    'MultipleSubsetsReportAggregationError("Report aggregation on multiple subsets:'
                ):
                    raise MultipleSubsetsReportAggregationError(
                        "Multiple subsets were used in the given pipeline runs. When this happens, "
                        "reports can't be aggregated. To fix this issue, retrieve reports for each "
                        "subset individually."
                    )
            raise AidkitClientError(
                error_message,
                error_details,
            )
        if not self.is_success:
            if self._is_augmentation_service_response(self.body):
                error_message = self.body["description"]  # type: ignore
                error_type = self.body["error_type"]  # type: ignore
                if error_type is AugmentationErrorType.AUGMENTATION_EXECUTION:
                    raise AugmentationExecutionError(error_message)
                if error_type is AugmentationErrorType.ALGORITHMIC:
                    raise AugmentationAlgorithmicError(error_message)
            raise AidkitClientError(
                error_message,
                error_details,
            )

    def body_bytes_or_error(self, error_message: str) -> bytes:
        """
        Return the body bytes if the response indicates success and is bytes,
        raise the appropriate error otherwise.

        :param error_message: Error message to prepend to the raised error if
            an error is raised. Must contain relevant context.
        :raises AuthenticationError: If the server returned a 401 status code.
        :raises ResourceWithNameNotFoundError: If the server returned a 404
            status code.
        :raises AidkitClientError: If some other error occured or if the server did
            not return a dictionary.
        :raises MultipleSubsetsReportAggregationError: If a report is retrieved for pipeline runs
            using different subsets.
        :return: Body of the response.
        """
        self._raise_error_based_on_status_code(error_message=error_message)
        if not isinstance(self.body, bytes):
            raise AidkitClientError(
                f"Server did not respond with bytes, but with content of type {type(self.body)}"
                f" and value {self.body}."
            )
        return self.body

    def body_dict_or_error(self, error_message: str) -> Dict[str, Any]:
        """
        Return the body dictionary if the response indicates success and is a
        dictionary, raise the appropriate error otherwise.

        :param error_message: Error message to prepend to the raised error if
            an error is raised. Must contain relevant context.
        :raises AuthenticationError: If the server returned a 401 status code.
        :raises ResourceWithNameNotFoundError: If the server returned a 404
            status code.
        :raises AidkitClientError: If some other error occured or if the server did
            not return a dictionary.
        :raises MultipleSubsetsReportAggregationError: If a report is retrieved for pipeline runs
            using different subsets.
        :return: Body of the response.
        """
        try:
            self._raise_error_based_on_status_code(error_message=error_message)
        except (ResourceWithNameNotFoundError, AuthenticationError) as exc:
            if isinstance(exc, AuthenticationError):
                if not exc.args[0] == "Server response: '{'message': '401 Unauthorized'}'":
                    raise exc
            raise AidkitClientError(
                "The connection to the server failed. Please make sure the configured API_URL "
                "is correct. For instructions on how to configure authentication, consult the documentation."
            ) from exc
        if isinstance(self.body, bytes):
            raise AidkitClientError(
                "Server did not respond with a dictionary but with bytes instead."
            )
        if not isinstance(self.body, dict):
            raise AidkitClientError(
                "Server did not respond with a dictionary, " f"but with the string '{self.body}'"
            )
        return self.body


class HTTPService(ABC):
    """
    Abstract HTTP service to use REST methods.
    """

    @abstractmethod
    async def get(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Get a resource on the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to get.
        :param parameters: Parameters to pass to the server.
        :returns: Response of the server.
        """

    @abstractmethod
    async def post_json(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[Any, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Post JSON data to the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be posted.
        :param parameters: Parameters to be passed to the server.
        :param parameters: Parameters to be passed to the server.
        :param body: JSON body to be posted to the server.
        :returns: Response of the server.
        """

    @abstractmethod
    async def post_multipart_data(
        self,
        path: str,
        data: Optional[Dict[Any, Any]] = None,
        files: Optional[Dict[Any, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Post multipart data to the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be posted.
        :param data: Data to be uploaded to the server.
        :param files: Files to be uploaded to the server.
        :returns: Response of the server.
        """

    @abstractmethod
    async def patch(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[Any, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Patch a resource on the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be patched.
        :param parameters: Parameters to pass to the server.
        :param body: JSON body of the patch request.
        :returns: Response of the server.
        """

    @abstractmethod
    async def delete(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Delete a resource on the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be deleted.
        :param parameters: Parameters to pass to the server.
        :returns: Response of the server.
        """

    @abstractmethod
    async def get_from_cdn(self, url: str, headers: Optional[Dict[str, Any]] = None) -> Response:
        """
        Get a file from the content delivery network.

        :param headers: Headers for httpx.AsyncClient
        :param url: url to access
        :returns: Response of the server.
        """

    @abstractmethod
    async def __aenter__(self) -> "HTTPService":
        """
        Enter the context to use the aidkit api within.
        """

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: typing.Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        """
        Exit the context of the underlying HTTPX client.

        :param exc_type: Exception type, if an exception is the reason to exit
            the context.
        :param exc_value: Exception value, if an exception is the reason to exit
            the context.
        :param traceback: Traceback, if an exception is the reason to exit
            the context.
            the context
        :param exc_value: Exception value, if an exception is the reason to exit
            the context
        :param traceback: Traceback, if an exception is the reason to exit
            the context
        """


T = TypeVar("T")
P = ParamSpec("P")


def _catch_connect_error(
    func: Callable[P, Coroutine[Any, Any, T]],
) -> Callable[P, Coroutine[Any, Any, T]]:
    """
    Catch 'httpx.ConncectError' and raise 'AidkitClientError' instead.

    The 'AidkitClientError' raised provides information to the user that the
    API_URL is misconfigured.

    :param func: The asynchronuous function to decorate.
    :returns: The decorated function.
    """

    @functools.wraps(func)
    async def wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return await func(*args, **kwargs)
        except httpx.ConnectError as exc:
            raise AidkitClientError(
                "The connection to the server failed. Please make sure the configured API_URL "
                "is correct. For instructions on how to configure authentication, consult the documentation."
            ) from exc

    return wrapped


class AidkitApi(HTTPService):
    """
    HTTP Service to be used to communicate with an aidkit server.
    """

    client: httpx.AsyncClient

    def __init__(self, client: httpx.AsyncClient) -> None:
        """
        Create a new instance configured with a base URL and a JWT auth token.

        :param client: HTTPX Async Client to use
        """
        self.client = client

    async def __aenter__(self) -> "AidkitApi":
        """
        Enter the context to use the aidkit api within.

        :return: AidkitApi this method is called on.
        """
        await self.client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: typing.Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        """
        Exit the context of the underlying HTTPX client.

        :param exc_type: Exception type, if an exception is the reason to exit
            the context.
        :param exc_value: Exception value, if an exception is the reason to exit
            the context.
        :param traceback: Traceback, if an exception is the reason to exit
            the context.
            the context
        :param exc_value: Exception value, if an exception is the reason to exit
            the context
        :param traceback: Traceback, if an exception is the reason to exit
            the context
        """
        await self.client.__aexit__(exc_type=exc_type, exc_value=exc_value, traceback=traceback)

    @_catch_connect_error
    async def get(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Get a resource on the server.

        :param path: Path of the resource to get.
        :param parameters: Parameters to pass to the server.
        :param headers: Headers for httpx.AsyncClient
        :returns: Response of the server.
        """
        response = await self.client.get(url=path, params=parameters or {}, headers=headers or {})
        return self._to_aidkit_response(response)

    @_catch_connect_error
    async def get_from_cdn(self, url: str, headers: Optional[Dict[str, Any]] = None) -> Response:
        """
        Get a file from the content delivery network.

        :param url: url to access
        :param headers: Headers for httpx.AsyncClient
        :returns: Response of the server.
        """
        res = await self.client.get(url=url, headers=headers or {})

        return Response(
            status_code=res.status_code,
            body={"content": res.content},
        )

    @_catch_connect_error
    async def post_json(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Post JSON data to the server.

        :param path: Path of the resource to be posted.
        :param parameters: Parameters to be passed to the server.
        :param body: JSON body to be posted to the server.
        :param headers: Headers for httpx.AsyncClient
        :returns: Response of the server.
        """
        response = await self.client.post(
            url=path, params=parameters or {}, json=body or {}, headers=headers or {}
        )
        return self._to_aidkit_response(response)

    @_catch_connect_error
    async def post_multipart_data(
        self,
        path: str,
        data: Optional[Dict[Any, Any]] = None,
        files: Optional[Dict[Any, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Post multipart data to the server.

        :param path: Path of the resource to be posted.
        :param data: Data to be uploaded to the server.
        :param files: Files to be uploaded to the server.
        :param headers: Headers for httpx.AsyncClient
        :returns: Response of the server.

        :raises HTTPXTimeoutException: Raised when httpx runs into a timeout.
        """
        try:
            response = await self.client.post(
                url=path, headers=headers or {}, data=data or {}, files=files or {}
            )
        except (
            httpx.PoolTimeout,
            httpx.ReadTimeout,
            httpx.WriteTimeout,
            httpx.ConnectTimeout,
        ) as exc:
            raise HTTPXTimeoutException(
                "httpx timeout occurred. Consider disabling or increasing the timeouts when setting up the client using `aidkit_client.configure`"
            ) from exc

        return self._to_aidkit_response(response)

    @_catch_connect_error
    async def patch(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Patch a resource on the server.

        :param path: Path of the resource to be patched.
        :param parameters: Parameters to pass to the server.
        :param body: JSON body of the patch request.
        :param headers: Headers for httpx.AsyncClient
        :returns: Response of the server.
        """
        response = await self.client.patch(
            url=path, params=parameters, json=body, headers=headers or {}
        )
        return self._to_aidkit_response(response)

    @_catch_connect_error
    async def delete(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Delete a resource on the server.

        :param path: Path of the resource to be deleted.
        :param parameters: Parameters to pass to the server.
        :param headers: Headers for httpx.AsyncClient
        :returns: Response of the server.
        """
        response = await self.client.delete(url=path, params=parameters, headers=headers or {})
        return self._to_aidkit_response(response)

    @classmethod
    def _to_aidkit_response(cls, res: httpx.Response) -> Response:
        if "content-type" in res.headers and res.headers["content-type"] == "image/png":
            return Response(status_code=res.status_code, body=res.read())

        if "content-type" in res.headers and res.headers["content-type"] == "text/html":
            raise AidkitClientError(
                "Invalid response recieved from the server. This is likely due to a wrong API URL "
                "set when configuring aidkit client. Make sure the API URL provided to the "
                "'base_url' parameter of aidkit's 'configure()' function is correct."
            )
        try:
            return Response(status_code=res.status_code, body=res.json())
        except json.decoder.JSONDecodeError:
            message = res.read().decode("utf-8")
            return Response(status_code=res.status_code, body=message)
        except UnicodeDecodeError as unicode_decode_exception:
            raise AidkitClientError(
                "The response retrieved from the server cannot be decoded."
            ) from unicode_decode_exception


class AuthorizingHTTPService(HTTPService):
    """
    HTTP Service to be used to communicate with an aidkit server.
    """

    _internal_http_service: HTTPService
    _authenticator_service: AuthenticatorService
    jwt_token: Union[str, asyncio.Task]

    def __init__(
        self,
        _internal_http_service: HTTPService,
        _authenticator_service: AuthenticatorService,
        auth_secret: str,
    ) -> None:
        """
        Create a new instance configured with a base URL and a JWT auth token.

        :param auth_secret: Auth secret for exchanging to JWT
        :param _authenticator_service: authenticator service
        :param _internal_http_service: The AidkitApi service to call
        """
        self._internal_http_service = _internal_http_service
        self.auth_url = self._construct_auth_url_from_application_id(auth_secret)
        self.auth_secret = auth_secret
        self._authenticator_service = _authenticator_service
        self.jwt_token = ""  # noqa: S105

    async def __aenter__(self) -> "HTTPService":
        """
        Enter the context to use the aidkit api within.

        :return: HTTPService this method is called on.
        """
        result = await self._internal_http_service.__aenter__()
        return result

    async def __aexit__(
        self,
        exc_type: typing.Type[BaseException],
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        """
        Exit the context of the underlying HTTPX client.

        :param exc_type: Exception type, if an exception is the reason to exit
            the context.
        :param exc_value: Exception value, if an exception is the reason to exit
            the context.
        :param traceback: Traceback, if an exception is the reason to exit
            the context.
            the context
        :param exc_value: Exception value, if an exception is the reason to exit
            the context
        :param traceback: Traceback, if an exception is the reason to exit
            the context
        """
        await self._internal_http_service.__aexit__(
            exc_type=exc_type, exc_value=exc_value, traceback=traceback
        )

    async def with_renew_token_and_retry(self, func: Callable) -> Response:
        """
        This will call the passed function, and check if the response is a 401.
        If this is the case, the JWT token will be renewed and the call will be
        repeated. In both cases the response is the response of the Callable.

        :param func: function to call
        :returns: function Response, identical to the response of the param func
        """
        result = await func()
        if result.status_code == 401:
            self.jwt_token = await self._authenticator_service.resolve_secret_to_access_token(
                self.auth_secret, self.auth_url
            )
            result = await func()

        return result

    async def get(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Get a resource on the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to get.
        :param parameters: Parameters to pass to the server.
        :returns: Response of the server.
        """

        async def perform() -> Response:
            return await self._internal_http_service.get(
                path=path, parameters=parameters, headers=await self._get_headers()
            )

        return await self.with_renew_token_and_retry(func=perform)

    async def get_from_cdn(self, url: str, headers: Optional[Dict[str, Any]] = None) -> Response:
        """
        Get a file from the content delivery network.

        :param headers: Headers for httpx.AsyncClient
        :param url: url to access
        :returns: Response of the server.
        """

        async def perform() -> Response:
            return await self._internal_http_service.get_from_cdn(
                url=url, headers=await self._get_headers()
            )

        return await self.with_renew_token_and_retry(func=perform)

    async def post_json(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Post JSON data to the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be posted.
        :param parameters: Parameters to be passed to the server.
        :param body: JSON body to be posted to the server.
        :returns: Response of the server.
        """

        async def perform() -> Response:
            return await self._internal_http_service.post_json(
                path=path,
                headers=await self._get_headers(),
                parameters=parameters,
                body=body,
            )

        return await self.with_renew_token_and_retry(func=perform)

    async def post_multipart_data(
        self,
        path: str,
        data: Optional[Dict[Any, Any]] = None,
        files: Optional[Dict[Any, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Post multipart data to the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be posted.
        :param data: Data to be uploaded to the server.
        :param files: Files to be uploaded to the server.
        :returns: Response of the server.
        """

        async def perform() -> Response:
            return await self._internal_http_service.post_multipart_data(
                path=path,
                headers=await self._get_headers(),
                data=data,
                files=files or {},
            )

        return await self.with_renew_token_and_retry(func=perform)

    async def patch(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Patch a resource on the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be patched.
        :param parameters: Parameters to pass to the server.
        :param body: JSON body of the patch request.
        :returns: Response of the server.
        """

        async def perform() -> Response:
            return await self._internal_http_service.patch(
                path=path,
                parameters=parameters,
                body=body,
                headers=await self._get_headers(),
            )

        return await self.with_renew_token_and_retry(func=perform)

    async def delete(
        self,
        path: str,
        parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        """
        Delete a resource on the server.

        :param headers: Headers for httpx.AsyncClient
        :param path: Path of the resource to be deleted.
        :param parameters: Parameters to pass to the server.
        :returns: Response of the server.
        """

        async def perform() -> Response:
            return await self._internal_http_service.delete(
                path=path, headers=await self._get_headers(), parameters=parameters
            )

        return await self.with_renew_token_and_retry(func=perform)

    async def _get_headers(self) -> Dict:
        if self.jwt_token == "":  # noqa: S105
            self.jwt_token = await self._authenticator_service.resolve_secret_to_access_token(
                self.auth_secret, self.auth_url
            )
        return {
            "Authorization": f"Bearer {self.jwt_token}",
            "api_version": API_VERSION,
        }

    @classmethod
    def _construct_auth_url_from_application_id(cls, api_secret: str) -> str:
        """
        Takes the first part of the api_secret (app_id:app_secret), which
        contains the Application ID, and constructs the auth url for Cognito.

        :param api_secret: API secret
        :returns: Constructed authentication URL.
        :raises AuthenticationError: If the server returned a 401 status code.
        :raises AidkitClientError: If the decoding of the 'api_secret' failed.
        """
        app = api_secret.split(":")
        if len(app) != 2:
            raise AidkitClientError(
                "The decoding of the 'auth_secret' failed. "
                "The 'auth_secret' is not of the expected format. "
                "Please make sure you have copied over the correct Authentication Token. "
                "Also see the documentation for more information on how to "
                "configure the client correctly."
            )
        if app[0] and isinstance(app[0], str) and app[1]:
            return f"https://{app[0]}.auth.eu-central-1.amazoncognito.com/oauth2/token"

        raise AuthenticationError("Unable to parse API URL")
