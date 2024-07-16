# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["OperationExecutionCreateParams", "Config", "FunctionProvider"]


class OperationExecutionCreateParams(TypedDict, total=False):
    api: Required[str]

    body: Required[Optional[object]]

    config: Required[Config]
    """Represents the API configuration for a plugin."""

    function_provider: Required[FunctionProvider]

    header: Required[Optional[object]]

    method: Required[str]

    path: Required[str]

    plugin_op_property_map: Required[Optional[Dict[str, Dict[str, object]]]]

    query_params: Required[Optional[object]]

    response_obj_200: Required[Optional[object]]

    enable_ui_form_controls: bool


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
