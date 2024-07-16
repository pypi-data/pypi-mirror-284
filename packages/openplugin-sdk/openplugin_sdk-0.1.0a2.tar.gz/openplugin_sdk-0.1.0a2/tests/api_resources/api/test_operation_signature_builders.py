# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openplugin import Openplugin, AsyncOpenplugin
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperationSignatureBuilders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Openplugin) -> None:
        operation_signature_builder = client.api.operation_signature_builders.create(
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
        )
        assert_matches_type(object, operation_signature_builder, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Openplugin) -> None:
        operation_signature_builder = client.api.operation_signature_builders.create(
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
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
            pipeline_name="pipeline_name",
            pre_prompts=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            selected_operation="selected_operation",
        )
        assert_matches_type(object, operation_signature_builder, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Openplugin) -> None:
        response = client.api.operation_signature_builders.with_raw_response.create(
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation_signature_builder = response.parse()
        assert_matches_type(object, operation_signature_builder, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Openplugin) -> None:
        with client.api.operation_signature_builders.with_streaming_response.create(
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation_signature_builder = response.parse()
            assert_matches_type(object, operation_signature_builder, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOperationSignatureBuilders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenplugin) -> None:
        operation_signature_builder = await async_client.api.operation_signature_builders.create(
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
        )
        assert_matches_type(object, operation_signature_builder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenplugin) -> None:
        operation_signature_builder = await async_client.api.operation_signature_builders.create(
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
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
            pipeline_name="pipeline_name",
            pre_prompts=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            selected_operation="selected_operation",
        )
        assert_matches_type(object, operation_signature_builder, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenplugin) -> None:
        response = await async_client.api.operation_signature_builders.with_raw_response.create(
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation_signature_builder = await response.parse()
        assert_matches_type(object, operation_signature_builder, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenplugin) -> None:
        async with async_client.api.operation_signature_builders.with_streaming_response.create(
            config={},
            function_provider={
                "name": "name",
                "required_auth_keys": [{}],
                "type": "type",
            },
            messages=[
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
                {
                    "content": "content",
                    "message_type": "HumanMessage",
                },
            ],
            plugin_manifest_url="plugin_manifest_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation_signature_builder = await response.parse()
            assert_matches_type(object, operation_signature_builder, path=["response"])

        assert cast(Any, response.is_closed) is True
