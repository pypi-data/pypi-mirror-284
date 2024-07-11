# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PageDoParams", "BrowseConfig", "Inventory"]


class PageDoParams(TypedDict, total=False):
    browser_session: Required[Annotated[str, PropertyInfo(alias="browserSession")]]

    browse_config: Required[BrowseConfig]

    headless: bool

    inventory: Iterable[Inventory]

    response_type: Optional[object]


class BrowseConfig(TypedDict, total=False):
    max_iterations: Required[Annotated[int, PropertyInfo(alias="maxIterations")]]

    objective: Required[List[str]]

    start_url: Required[Annotated[str, PropertyInfo(alias="startUrl")]]


class Inventory(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["string", "number"]]

    value: Required[str]
