# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PageStepResponse", "State"]


class State(BaseModel):
    aria_tree: str = FieldInfo(alias="ariaTree")

    kind: Literal["ObjectiveState"]

    objective: str

    progress: List[str]

    url: str


class PageStepResponse(BaseModel):
    state: State

    result: Optional[object] = None
