# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ContentRetrieveResponse"]


class ContentRetrieveResponse(BaseModel):
    page_content: str = FieldInfo(alias="pageContent")

    type: Literal["markdown", "html", "text"]

    url: str
