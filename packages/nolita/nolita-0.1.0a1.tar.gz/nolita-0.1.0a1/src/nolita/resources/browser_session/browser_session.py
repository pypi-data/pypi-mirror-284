# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .page import (
    PageResource,
    AsyncPageResource,
    PageResourceWithRawResponse,
    AsyncPageResourceWithRawResponse,
    PageResourceWithStreamingResponse,
    AsyncPageResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.browser_session_close_response import BrowserSessionCloseResponse

__all__ = ["BrowserSessionResource", "AsyncBrowserSessionResource"]


class BrowserSessionResource(SyncAPIResource):
    @cached_property
    def page(self) -> PageResource:
        return PageResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowserSessionResourceWithRawResponse:
        return BrowserSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserSessionResourceWithStreamingResponse:
        return BrowserSessionResourceWithStreamingResponse(self)

    def close(
        self,
        browser_session: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserSessionCloseResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        return self._get(
            f"/browser/{browser_session}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionCloseResponse,
        )


class AsyncBrowserSessionResource(AsyncAPIResource):
    @cached_property
    def page(self) -> AsyncPageResource:
        return AsyncPageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserSessionResourceWithRawResponse:
        return AsyncBrowserSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserSessionResourceWithStreamingResponse:
        return AsyncBrowserSessionResourceWithStreamingResponse(self)

    async def close(
        self,
        browser_session: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrowserSessionCloseResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        return await self._get(
            f"/browser/{browser_session}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionCloseResponse,
        )


class BrowserSessionResourceWithRawResponse:
    def __init__(self, browser_session: BrowserSessionResource) -> None:
        self._browser_session = browser_session

        self.close = to_raw_response_wrapper(
            browser_session.close,
        )

    @cached_property
    def page(self) -> PageResourceWithRawResponse:
        return PageResourceWithRawResponse(self._browser_session.page)


class AsyncBrowserSessionResourceWithRawResponse:
    def __init__(self, browser_session: AsyncBrowserSessionResource) -> None:
        self._browser_session = browser_session

        self.close = async_to_raw_response_wrapper(
            browser_session.close,
        )

    @cached_property
    def page(self) -> AsyncPageResourceWithRawResponse:
        return AsyncPageResourceWithRawResponse(self._browser_session.page)


class BrowserSessionResourceWithStreamingResponse:
    def __init__(self, browser_session: BrowserSessionResource) -> None:
        self._browser_session = browser_session

        self.close = to_streamed_response_wrapper(
            browser_session.close,
        )

    @cached_property
    def page(self) -> PageResourceWithStreamingResponse:
        return PageResourceWithStreamingResponse(self._browser_session.page)


class AsyncBrowserSessionResourceWithStreamingResponse:
    def __init__(self, browser_session: AsyncBrowserSessionResource) -> None:
        self._browser_session = browser_session

        self.close = async_to_streamed_response_wrapper(
            browser_session.close,
        )

    @cached_property
    def page(self) -> AsyncPageResourceWithStreamingResponse:
        return AsyncPageResourceWithStreamingResponse(self._browser_session.page)
