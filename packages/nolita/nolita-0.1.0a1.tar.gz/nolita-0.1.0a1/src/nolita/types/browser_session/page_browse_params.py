# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PageBrowseParams"]


class PageBrowseParams(TypedDict, total=False):
    browser_session: Required[Annotated[str, PropertyInfo(alias="browserSession")]]

    command: Required[str]

    max_turns: Required[Annotated[float, PropertyInfo(alias="maxTurns")]]

    inventory: Dict[str, str]

    schema: Optional[object]
