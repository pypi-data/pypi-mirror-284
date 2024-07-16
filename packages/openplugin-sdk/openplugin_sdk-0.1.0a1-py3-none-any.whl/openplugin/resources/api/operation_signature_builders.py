# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ...types.api import operation_signature_builder_create_params
from ..._base_client import make_request_options

__all__ = ["OperationSignatureBuildersResource", "AsyncOperationSignatureBuildersResource"]


class OperationSignatureBuildersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationSignatureBuildersResourceWithRawResponse:
        return OperationSignatureBuildersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationSignatureBuildersResourceWithStreamingResponse:
        return OperationSignatureBuildersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: operation_signature_builder_create_params.Config,
        function_provider: operation_signature_builder_create_params.FunctionProvider,
        messages: Iterable[operation_signature_builder_create_params.Message],
        plugin_manifest_url: str,
        pipeline_name: Optional[str] | NotGiven = NOT_GIVEN,
        pre_prompts: Optional[Iterable[operation_signature_builder_create_params.PrePrompt]] | NotGiven = NOT_GIVEN,
        selected_operation: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Operation Signature Builder

        Args:
          config: Represents the API configuration for a plugin.

          pipeline_name: pipeline_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/operation-signature-builder",
            body=maybe_transform(
                {
                    "config": config,
                    "function_provider": function_provider,
                    "messages": messages,
                    "plugin_manifest_url": plugin_manifest_url,
                    "pre_prompts": pre_prompts,
                    "selected_operation": selected_operation,
                },
                operation_signature_builder_create_params.OperationSignatureBuilderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"pipeline_name": pipeline_name},
                    operation_signature_builder_create_params.OperationSignatureBuilderCreateParams,
                ),
            ),
            cast_to=object,
        )


class AsyncOperationSignatureBuildersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationSignatureBuildersResourceWithRawResponse:
        return AsyncOperationSignatureBuildersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationSignatureBuildersResourceWithStreamingResponse:
        return AsyncOperationSignatureBuildersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: operation_signature_builder_create_params.Config,
        function_provider: operation_signature_builder_create_params.FunctionProvider,
        messages: Iterable[operation_signature_builder_create_params.Message],
        plugin_manifest_url: str,
        pipeline_name: Optional[str] | NotGiven = NOT_GIVEN,
        pre_prompts: Optional[Iterable[operation_signature_builder_create_params.PrePrompt]] | NotGiven = NOT_GIVEN,
        selected_operation: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Operation Signature Builder

        Args:
          config: Represents the API configuration for a plugin.

          pipeline_name: pipeline_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/operation-signature-builder",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "function_provider": function_provider,
                    "messages": messages,
                    "plugin_manifest_url": plugin_manifest_url,
                    "pre_prompts": pre_prompts,
                    "selected_operation": selected_operation,
                },
                operation_signature_builder_create_params.OperationSignatureBuilderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"pipeline_name": pipeline_name},
                    operation_signature_builder_create_params.OperationSignatureBuilderCreateParams,
                ),
            ),
            cast_to=object,
        )


class OperationSignatureBuildersResourceWithRawResponse:
    def __init__(self, operation_signature_builders: OperationSignatureBuildersResource) -> None:
        self._operation_signature_builders = operation_signature_builders

        self.create = to_raw_response_wrapper(
            operation_signature_builders.create,
        )


class AsyncOperationSignatureBuildersResourceWithRawResponse:
    def __init__(self, operation_signature_builders: AsyncOperationSignatureBuildersResource) -> None:
        self._operation_signature_builders = operation_signature_builders

        self.create = async_to_raw_response_wrapper(
            operation_signature_builders.create,
        )


class OperationSignatureBuildersResourceWithStreamingResponse:
    def __init__(self, operation_signature_builders: OperationSignatureBuildersResource) -> None:
        self._operation_signature_builders = operation_signature_builders

        self.create = to_streamed_response_wrapper(
            operation_signature_builders.create,
        )


class AsyncOperationSignatureBuildersResourceWithStreamingResponse:
    def __init__(self, operation_signature_builders: AsyncOperationSignatureBuildersResource) -> None:
        self._operation_signature_builders = operation_signature_builders

        self.create = async_to_streamed_response_wrapper(
            operation_signature_builders.create,
        )
