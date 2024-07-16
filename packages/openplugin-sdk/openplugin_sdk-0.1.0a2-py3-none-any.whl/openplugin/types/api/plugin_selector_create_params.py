# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PluginSelectorCreateParams", "Config", "Message"]


class PluginSelectorCreateParams(TypedDict, total=False):
    config: Required[Config]
    """Represents the API configuration for a plugin."""

    messages: Required[Iterable[Message]]

    openplugin_manifest_urls: Required[List[str]]

    pipeline_name: Required[str]


class Config(TypedDict, total=False):
    anthropic_api_key: Optional[str]

    aws_access_key_id: Optional[str]

    aws_region_name: Optional[str]

    aws_secret_access_key: Optional[str]

    azure_api_key: Optional[str]

    cohere_api_key: Optional[str]

    fireworks_api_key: Optional[str]

    gemini_api_key: Optional[str]

    google_palm_key: Optional[str]

    groq_api_key: Optional[str]

    mistral_api_key: Optional[str]

    openai_api_key: Optional[str]

    provider: str

    together_api_key: Optional[str]


class Message(TypedDict, total=False):
    content: Required[str]

    message_type: Required[Literal["HumanMessage", "AIMessage", "SystemMessage", "FunctionMessage"]]
