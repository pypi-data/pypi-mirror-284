# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PageDoResponse"]


class PageDoResponse(BaseModel):
    aria_tree: str = FieldInfo(alias="ariaTree")

    kind: Literal["ObjectiveState"]

    objective: str

    progress: List[str]

    url: str
