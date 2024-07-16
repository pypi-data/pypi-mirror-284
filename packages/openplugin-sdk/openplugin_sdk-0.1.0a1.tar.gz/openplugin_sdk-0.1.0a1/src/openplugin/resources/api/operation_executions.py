# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

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
from ...types.api import operation_execution_create_params
from ..._base_client import make_request_options

__all__ = ["OperationExecutionsResource", "AsyncOperationExecutionsResource"]


class OperationExecutionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationExecutionsResourceWithRawResponse:
        return OperationExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationExecutionsResourceWithStreamingResponse:
        return OperationExecutionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        api: str,
        body: Optional[object],
        config: operation_execution_create_params.Config,
        function_provider: operation_execution_create_params.FunctionProvider,
        header: Optional[object],
        method: str,
        path: str,
        plugin_op_property_map: Optional[Dict[str, Dict[str, object]]],
        query_params: Optional[object],
        response_obj_200: Optional[object],
        enable_ui_form_controls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Operation Execution

        Args:
          config: Represents the API configuration for a plugin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/operation-execution",
            body=maybe_transform(
                {
                    "api": api,
                    "body": body,
                    "config": config,
                    "function_provider": function_provider,
                    "header": header,
                    "method": method,
                    "path": path,
                    "plugin_op_property_map": plugin_op_property_map,
                    "query_params": query_params,
                    "response_obj_200": response_obj_200,
                    "enable_ui_form_controls": enable_ui_form_controls,
                },
                operation_execution_create_params.OperationExecutionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOperationExecutionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationExecutionsResourceWithRawResponse:
        return AsyncOperationExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationExecutionsResourceWithStreamingResponse:
        return AsyncOperationExecutionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        api: str,
        body: Optional[object],
        config: operation_execution_create_params.Config,
        function_provider: operation_execution_create_params.FunctionProvider,
        header: Optional[object],
        method: str,
        path: str,
        plugin_op_property_map: Optional[Dict[str, Dict[str, object]]],
        query_params: Optional[object],
        response_obj_200: Optional[object],
        enable_ui_form_controls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Operation Execution

        Args:
          config: Represents the API configuration for a plugin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/operation-execution",
            body=await async_maybe_transform(
                {
                    "api": api,
                    "body": body,
                    "config": config,
                    "function_provider": function_provider,
                    "header": header,
                    "method": method,
                    "path": path,
                    "plugin_op_property_map": plugin_op_property_map,
                    "query_params": query_params,
                    "response_obj_200": response_obj_200,
                    "enable_ui_form_controls": enable_ui_form_controls,
                },
                operation_execution_create_params.OperationExecutionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OperationExecutionsResourceWithRawResponse:
    def __init__(self, operation_executions: OperationExecutionsResource) -> None:
        self._operation_executions = operation_executions

        self.create = to_raw_response_wrapper(
            operation_executions.create,
        )


class AsyncOperationExecutionsResourceWithRawResponse:
    def __init__(self, operation_executions: AsyncOperationExecutionsResource) -> None:
        self._operation_executions = operation_executions

        self.create = async_to_raw_response_wrapper(
            operation_executions.create,
        )


class OperationExecutionsResourceWithStreamingResponse:
    def __init__(self, operation_executions: OperationExecutionsResource) -> None:
        self._operation_executions = operation_executions

        self.create = to_streamed_response_wrapper(
            operation_executions.create,
        )


class AsyncOperationExecutionsResourceWithStreamingResponse:
    def __init__(self, operation_executions: AsyncOperationExecutionsResource) -> None:
        self._operation_executions = operation_executions

        self.create = async_to_streamed_response_wrapper(
            operation_executions.create,
        )
