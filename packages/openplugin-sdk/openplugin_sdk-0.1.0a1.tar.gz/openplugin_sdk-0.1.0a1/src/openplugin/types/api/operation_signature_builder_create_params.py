# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationSignatureBuilderCreateParams", "Config", "FunctionProvider", "Message", "PrePrompt"]


class OperationSignatureBuilderCreateParams(TypedDict, total=False):
    config: Required[Config]
    """Represents the API configuration for a plugin."""

    function_provider: Required[FunctionProvider]

    messages: Required[Iterable[Message]]

    plugin_manifest_url: Required[str]

    pipeline_name: Optional[str]
    """pipeline_name"""

    pre_prompts: Optional[Iterable[PrePrompt]]

    selected_operation: Optional[str]


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


class FunctionProvider(TypedDict, total=False):
    name: Required[str]

    required_auth_keys: Required[Iterable[object]]

    type: Required[str]

    is_default: bool

    is_supported: bool


class Message(TypedDict, total=False):
    content: Required[str]

    message_type: Required[Literal["HumanMessage", "AIMessage", "SystemMessage", "FunctionMessage"]]


class PrePrompt(TypedDict, total=False):
    content: Required[str]

    message_type: Required[Literal["HumanMessage", "AIMessage", "SystemMessage", "FunctionMessage"]]
