# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PageListResponse", "PageListResponseItem"]


class PageListResponseItem(BaseModel):
    id: str

    title: str

    url: str

    progress: Optional[List[str]] = None


PageListResponse = List[PageListResponseItem]
