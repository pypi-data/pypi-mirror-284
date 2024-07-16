# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openplugin import Openplugin, AsyncOpenplugin
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPluginSelectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Openplugin) -> None:
        plugin_selector = client.api.plugin_selectors.create(
            config={},
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        )
        assert_matches_type(object, plugin_selector, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Openplugin) -> None:
        plugin_selector = client.api.plugin_selectors.create(
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        )
        assert_matches_type(object, plugin_selector, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Openplugin) -> None:
        response = client.api.plugin_selectors.with_raw_response.create(
            config={},
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin_selector = response.parse()
        assert_matches_type(object, plugin_selector, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Openplugin) -> None:
        with client.api.plugin_selectors.with_streaming_response.create(
            config={},
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin_selector = response.parse()
            assert_matches_type(object, plugin_selector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPluginSelectors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenplugin) -> None:
        plugin_selector = await async_client.api.plugin_selectors.create(
            config={},
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        )
        assert_matches_type(object, plugin_selector, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenplugin) -> None:
        plugin_selector = await async_client.api.plugin_selectors.create(
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        )
        assert_matches_type(object, plugin_selector, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenplugin) -> None:
        response = await async_client.api.plugin_selectors.with_raw_response.create(
            config={},
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin_selector = await response.parse()
        assert_matches_type(object, plugin_selector, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenplugin) -> None:
        async with async_client.api.plugin_selectors.with_streaming_response.create(
            config={},
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
            openplugin_manifest_urls=["string", "string", "string"],
            pipeline_name="pipeline_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin_selector = await response.parse()
            assert_matches_type(object, plugin_selector, path=["response"])

        assert cast(Any, response.is_closed) is True
