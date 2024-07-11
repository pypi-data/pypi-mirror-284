# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ObjectiveComplete"]


class ObjectiveComplete(BaseModel):
    kind: Literal["ObjectiveComplete"]
    """Objective is complete"""

    result: str
    """The result of the objective"""

    response_type: Optional[object] = None
