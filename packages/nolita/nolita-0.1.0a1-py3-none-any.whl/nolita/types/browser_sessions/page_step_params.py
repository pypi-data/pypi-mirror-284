# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PageStepParams", "Opts"]


class PageStepParams(TypedDict, total=False):
    browser_session: Required[Annotated[str, PropertyInfo(alias="browserSession")]]

    command: Required[str]

    opts: Opts

    schema: Optional[object]


class Opts(TypedDict, total=False):
    delay: float

    inventory: Dict[str, str]
