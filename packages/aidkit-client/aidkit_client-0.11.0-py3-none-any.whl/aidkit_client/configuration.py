"""
Utilities to configure the aidkit python client.
"""

import logging
import os
from typing import Dict, Optional, Union

import altair as alt
import httpx
from dotenv import dotenv_values

from aidkit_client.aidkit_api import (
    API_VERSION,
    AidkitApi,
    AuthorizingHTTPService,
    HTTPService,
)
from aidkit_client.authenticator import ExternalAuthenticatorService
from aidkit_client.exceptions import (
    AidkitClientNotConfiguredError,
)
from aidkit_client.plotting.plot_renderer import aidkit_altair_plot_renderer

_DEFAULT_TIMEOUT: Union[int, httpx.Timeout] = 300

LOG = logging.getLogger(__name__)

# keep this for backwards test compatibility
_GLOBAL_API_SERVICE: Optional[HTTPService] = None
_API_URL: Optional[str] = None
_AUTH_SECRET: Optional[str] = None


def configure(
    base_url: str,
    auth_secret: str,
    timeout: Union[int, httpx.Timeout] = _DEFAULT_TIMEOUT,
    global_api_service: bool = True,
) -> None:
    """
    Configure the client. Must be called before the client is used.

    :param base_url: Base URL of the API backend.
    :param auth_secret: API secret for authentication.
    :param timeout: Timeout for HTTP requests in seconds or `httpx.Timeout` object. For long-running
                    requests you might want to disable some timeouts by setting this value to
                    `httpx.Timeout(connect=10, read=None, write=None, pool=None)`, for example.
    :param global_api_service: if true, one API service will be shared with all resources. Set to false in
         multi-threaded environments.
    """
    global _API_URL  # pylint: disable=global-statement
    global _AUTH_SECRET  # pylint: disable=global-statement

    _API_URL = base_url
    _AUTH_SECRET = auth_secret

    if global_api_service:
        global _GLOBAL_API_SERVICE  # pylint: disable=global-statement
        aidkit_api = AidkitApi(
            httpx.AsyncClient(
                base_url=base_url, timeout=timeout, headers={"api_version": API_VERSION}
            )
        )
        authenticator = ExternalAuthenticatorService(
            httpx.AsyncClient(timeout=30), access_token_cache=False
        )
        _GLOBAL_API_SERVICE = AuthorizingHTTPService(
            auth_secret=auth_secret,
            _internal_http_service=aidkit_api,
            _authenticator_service=authenticator,
        )

    # Initialize the renderer for the plots
    alt.renderers.register("aidkit_renderer", aidkit_altair_plot_renderer)
    # TODO: https://neurocats.atlassian.net/browse/AK-4810
    alt.renderers.enable("default")


def _get_config() -> Dict[str, Optional[str]]:
    if _API_URL and _AUTH_SECRET:
        local_config = {"API_URL": _API_URL, "AUTH_SECRET": _AUTH_SECRET}
    else:
        local_config = {}

    config = {
        **dotenv_values(".env"),
        **dotenv_values(".env.local"),
        **os.environ,  # override loaded values with environment variables
        **local_config,
    }
    return config


def get_api_client(access_token_cache: bool = True) -> HTTPService:
    """
    Get an API client with API_URL and AUTH_SECRET variables.

    These variables are read in order of priority:
    configure function > os environment variable > .env.local > .env

    :param access_token_cache: cache the authentication token. Useful to avoid too many requests
        to the authentication provider.
    :raises AidkitClientNotConfiguredError: If the API_URL or AUTH_SECRET is not found.
    :return: Service instance.
    """
    config = _get_config()

    # for legacy tests that patch _GLOBAL_API_SERVICE
    if _GLOBAL_API_SERVICE:
        return _GLOBAL_API_SERVICE

    api_url = config.get("API_URL")
    auth_secret = config.get("AUTH_SECRET")

    if api_url and auth_secret:
        LOG.info(
            f"Connection configuration\n - API_URL: {api_url}\n - AUTH_SECRET: {auth_secret[:5]}xxxxxxxxxxxxxx"
        )

        aidkit_api = AidkitApi(
            httpx.AsyncClient(
                base_url=api_url, timeout=_DEFAULT_TIMEOUT, headers={"api_version": API_VERSION}
            )
        )
        authenticator = ExternalAuthenticatorService(
            httpx.AsyncClient(timeout=30), access_token_cache=access_token_cache
        )
        api_service = AuthorizingHTTPService(
            auth_secret=auth_secret,
            _internal_http_service=aidkit_api,
            _authenticator_service=authenticator,
        )
        return api_service
    else:
        raise AidkitClientNotConfiguredError(
            "The API_URL and AUTH_SECRET are not set. Add them to an .env"
            "file or use the `configure` function to set them"
        )
