# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openplugin import Openplugin, AsyncOpenplugin
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperationExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Openplugin) -> None:
        operation_execution = client.api.operation_executions.create(
            api="api",
            body={},
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
        )
        assert_matches_type(object, operation_execution, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Openplugin) -> None:
        operation_execution = client.api.operation_executions.create(
            api="api",
            body={},
            config={
                "provider": "provider",
                "openai_api_key": "openai_api_key",
                "cohere_api_key": "cohere_api_key",
                "mistral_api_key": "mistral_api_key",
                "fireworks_api_key": "fireworks_api_key",
                "google_palm_key": "google_palm_key",
                "gemini_api_key": "gemini_api_key",
                "anthropic_api_key": "anthropic_api_key",
                "together_api_key": "together_api_key",
                "aws_access_key_id": "aws_access_key_id",
                "aws_secret_access_key": "aws_secret_access_key",
                "aws_region_name": "aws_region_name",
                "azure_api_key": "azure_api_key",
                "groq_api_key": "groq_api_key",
            },
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
                "is_supported": True,
                "is_default": True,
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
            enable_ui_form_controls=True,
        )
        assert_matches_type(object, operation_execution, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Openplugin) -> None:
        response = client.api.operation_executions.with_raw_response.create(
            api="api",
            body={},
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation_execution = response.parse()
        assert_matches_type(object, operation_execution, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Openplugin) -> None:
        with client.api.operation_executions.with_streaming_response.create(
            api="api",
            body={},
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation_execution = response.parse()
            assert_matches_type(object, operation_execution, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOperationExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenplugin) -> None:
        operation_execution = await async_client.api.operation_executions.create(
            api="api",
            body={},
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
        )
        assert_matches_type(object, operation_execution, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenplugin) -> None:
        operation_execution = await async_client.api.operation_executions.create(
            api="api",
            body={},
            config={
                "provider": "provider",
                "openai_api_key": "openai_api_key",
                "cohere_api_key": "cohere_api_key",
                "mistral_api_key": "mistral_api_key",
                "fireworks_api_key": "fireworks_api_key",
                "google_palm_key": "google_palm_key",
                "gemini_api_key": "gemini_api_key",
                "anthropic_api_key": "anthropic_api_key",
                "together_api_key": "together_api_key",
                "aws_access_key_id": "aws_access_key_id",
                "aws_secret_access_key": "aws_secret_access_key",
                "aws_region_name": "aws_region_name",
                "azure_api_key": "azure_api_key",
                "groq_api_key": "groq_api_key",
            },
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
                "is_supported": True,
                "is_default": True,
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
            enable_ui_form_controls=True,
        )
        assert_matches_type(object, operation_execution, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenplugin) -> None:
        response = await async_client.api.operation_executions.with_raw_response.create(
            api="api",
            body={},
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation_execution = await response.parse()
        assert_matches_type(object, operation_execution, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenplugin) -> None:
        async with async_client.api.operation_executions.with_streaming_response.create(
            api="api",
            body={},
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            header={},
            method="method",
            path="path",
            plugin_op_property_map={"foo": {"foo": {}}},
            query_params={},
            response_obj_200={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation_execution = await response.parse()
            assert_matches_type(object, operation_execution, path=["response"])

        assert cast(Any, response.is_closed) is True
