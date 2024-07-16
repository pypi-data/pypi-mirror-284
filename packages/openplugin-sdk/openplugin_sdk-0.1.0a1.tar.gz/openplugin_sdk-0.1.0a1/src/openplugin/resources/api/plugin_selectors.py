# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import plugin_selector_create_params
from ..._base_client import make_request_options

__all__ = ["PluginSelectorsResource", "AsyncPluginSelectorsResource"]


class PluginSelectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PluginSelectorsResourceWithRawResponse:
        return PluginSelectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PluginSelectorsResourceWithStreamingResponse:
        return PluginSelectorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: plugin_selector_create_params.Config,
        messages: Iterable[plugin_selector_create_params.Message],
        openplugin_manifest_urls: List[str],
        pipeline_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Plugin Selector

        Args:
          config: Represents the API configuration for a plugin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/plugin-selector",
            body=maybe_transform(
                {
                    "config": config,
                    "messages": messages,
                    "openplugin_manifest_urls": openplugin_manifest_urls,
                    "pipeline_name": pipeline_name,
                },
                plugin_selector_create_params.PluginSelectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPluginSelectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPluginSelectorsResourceWithRawResponse:
        return AsyncPluginSelectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPluginSelectorsResourceWithStreamingResponse:
        return AsyncPluginSelectorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: plugin_selector_create_params.Config,
        messages: Iterable[plugin_selector_create_params.Message],
        openplugin_manifest_urls: List[str],
        pipeline_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Plugin Selector

        Args:
          config: Represents the API configuration for a plugin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/plugin-selector",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "messages": messages,
                    "openplugin_manifest_urls": openplugin_manifest_urls,
                    "pipeline_name": pipeline_name,
                },
                plugin_selector_create_params.PluginSelectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PluginSelectorsResourceWithRawResponse:
    def __init__(self, plugin_selectors: PluginSelectorsResource) -> None:
        self._plugin_selectors = plugin_selectors

        self.create = to_raw_response_wrapper(
            plugin_selectors.create,
        )


class AsyncPluginSelectorsResourceWithRawResponse:
    def __init__(self, plugin_selectors: AsyncPluginSelectorsResource) -> None:
        self._plugin_selectors = plugin_selectors

        self.create = async_to_raw_response_wrapper(
            plugin_selectors.create,
        )


class PluginSelectorsResourceWithStreamingResponse:
    def __init__(self, plugin_selectors: PluginSelectorsResource) -> None:
        self._plugin_selectors = plugin_selectors

        self.create = to_streamed_response_wrapper(
            plugin_selectors.create,
        )


class AsyncPluginSelectorsResourceWithStreamingResponse:
    def __init__(self, plugin_selectors: AsyncPluginSelectorsResource) -> None:
        self._plugin_selectors = plugin_selectors

        self.create = async_to_streamed_response_wrapper(
            plugin_selectors.create,
        )
