# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .pages.pages import PagesResource, AsyncPagesResource

__all__ = ["BrowserSessionsResource", "AsyncBrowserSessionsResource"]


class BrowserSessionsResource(SyncAPIResource):
    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowserSessionsResourceWithRawResponse:
        return BrowserSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserSessionsResourceWithStreamingResponse:
        return BrowserSessionsResourceWithStreamingResponse(self)


class AsyncBrowserSessionsResource(AsyncAPIResource):
    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserSessionsResourceWithRawResponse:
        return AsyncBrowserSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserSessionsResourceWithStreamingResponse:
        return AsyncBrowserSessionsResourceWithStreamingResponse(self)


class BrowserSessionsResourceWithRawResponse:
    def __init__(self, browser_sessions: BrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._browser_sessions.pages)


class AsyncBrowserSessionsResourceWithRawResponse:
    def __init__(self, browser_sessions: AsyncBrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._browser_sessions.pages)


class BrowserSessionsResourceWithStreamingResponse:
    def __init__(self, browser_sessions: BrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._browser_sessions.pages)


class AsyncBrowserSessionsResourceWithStreamingResponse:
    def __init__(self, browser_sessions: AsyncBrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._browser_sessions.pages)
