# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .contents import (
    ContentsResource,
    AsyncContentsResource,
    ContentsResourceWithRawResponse,
    AsyncContentsResourceWithRawResponse,
    ContentsResourceWithStreamingResponse,
    AsyncContentsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .screenshots import (
    ScreenshotsResource,
    AsyncScreenshotsResource,
    ScreenshotsResourceWithRawResponse,
    AsyncScreenshotsResourceWithRawResponse,
    ScreenshotsResourceWithStreamingResponse,
    AsyncScreenshotsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.browser_sessions import page_do_params, page_step_params
from ....types.browser_sessions.page_do_response import PageDoResponse
from ....types.browser_sessions.page_list_response import PageListResponse
from ....types.browser_sessions.page_step_response import PageStepResponse
from ....types.browser_sessions.page_close_response import PageCloseResponse
from ....types.browser_sessions.page_new_page_response import PageNewPageResponse
from ....types.browser_sessions.page_retrieve_response import PageRetrieveResponse

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def screenshots(self) -> ScreenshotsResource:
        return ScreenshotsResource(self._client)

    @cached_property
    def contents(self) -> ContentsResource:
        return ContentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        page_id: str,
        *,
        browser_session: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._get(
            f"/{browser_session}/page/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageRetrieveResponse,
        )

    def list(
        self,
        browser_session: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageListResponse:
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
            f"/{browser_session}/pages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageListResponse,
        )

    def close(
        self,
        page_id: str,
        *,
        browser_session: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageCloseResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._get(
            f"/{browser_session}/page/{page_id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageCloseResponse,
        )

    def do(
        self,
        page_id: str,
        *,
        browser_session: str,
        browse_config: page_do_params.BrowseConfig,
        headless: bool | NotGiven = NOT_GIVEN,
        inventory: Iterable[page_do_params.Inventory] | NotGiven = NOT_GIVEN,
        response_type: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageDoResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._post(
            f"/{browser_session}/page/{page_id}/do",
            body=maybe_transform(
                {
                    "browse_config": browse_config,
                    "headless": headless,
                    "inventory": inventory,
                    "response_type": response_type,
                },
                page_do_params.PageDoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageDoResponse,
        )

    def new_page(
        self,
        browser_session: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageNewPageResponse:
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
            f"/{browser_session}/page/newPage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageNewPageResponse,
        )

    def step(
        self,
        page_id: str,
        *,
        browser_session: str,
        command: str,
        opts: page_step_params.Opts | NotGiven = NOT_GIVEN,
        schema: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageStepResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return self._post(
            f"/{browser_session}/page/{page_id}/step",
            body=maybe_transform(
                {
                    "command": command,
                    "opts": opts,
                    "schema": schema,
                },
                page_step_params.PageStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageStepResponse,
        )


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def screenshots(self) -> AsyncScreenshotsResource:
        return AsyncScreenshotsResource(self._client)

    @cached_property
    def contents(self) -> AsyncContentsResource:
        return AsyncContentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        page_id: str,
        *,
        browser_session: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._get(
            f"/{browser_session}/page/{page_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageRetrieveResponse,
        )

    async def list(
        self,
        browser_session: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageListResponse:
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
            f"/{browser_session}/pages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageListResponse,
        )

    async def close(
        self,
        page_id: str,
        *,
        browser_session: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageCloseResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._get(
            f"/{browser_session}/page/{page_id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageCloseResponse,
        )

    async def do(
        self,
        page_id: str,
        *,
        browser_session: str,
        browse_config: page_do_params.BrowseConfig,
        headless: bool | NotGiven = NOT_GIVEN,
        inventory: Iterable[page_do_params.Inventory] | NotGiven = NOT_GIVEN,
        response_type: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageDoResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._post(
            f"/{browser_session}/page/{page_id}/do",
            body=await async_maybe_transform(
                {
                    "browse_config": browse_config,
                    "headless": headless,
                    "inventory": inventory,
                    "response_type": response_type,
                },
                page_do_params.PageDoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageDoResponse,
        )

    async def new_page(
        self,
        browser_session: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageNewPageResponse:
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
            f"/{browser_session}/page/newPage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageNewPageResponse,
        )

    async def step(
        self,
        page_id: str,
        *,
        browser_session: str,
        command: str,
        opts: page_step_params.Opts | NotGiven = NOT_GIVEN,
        schema: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageStepResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not browser_session:
            raise ValueError(f"Expected a non-empty value for `browser_session` but received {browser_session!r}")
        if not page_id:
            raise ValueError(f"Expected a non-empty value for `page_id` but received {page_id!r}")
        return await self._post(
            f"/{browser_session}/page/{page_id}/step",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "opts": opts,
                    "schema": schema,
                },
                page_step_params.PageStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageStepResponse,
        )


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.retrieve = to_raw_response_wrapper(
            pages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            pages.list,
        )
        self.close = to_raw_response_wrapper(
            pages.close,
        )
        self.do = to_raw_response_wrapper(
            pages.do,
        )
        self.new_page = to_raw_response_wrapper(
            pages.new_page,
        )
        self.step = to_raw_response_wrapper(
            pages.step,
        )

    @cached_property
    def screenshots(self) -> ScreenshotsResourceWithRawResponse:
        return ScreenshotsResourceWithRawResponse(self._pages.screenshots)

    @cached_property
    def contents(self) -> ContentsResourceWithRawResponse:
        return ContentsResourceWithRawResponse(self._pages.contents)


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.retrieve = async_to_raw_response_wrapper(
            pages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            pages.list,
        )
        self.close = async_to_raw_response_wrapper(
            pages.close,
        )
        self.do = async_to_raw_response_wrapper(
            pages.do,
        )
        self.new_page = async_to_raw_response_wrapper(
            pages.new_page,
        )
        self.step = async_to_raw_response_wrapper(
            pages.step,
        )

    @cached_property
    def screenshots(self) -> AsyncScreenshotsResourceWithRawResponse:
        return AsyncScreenshotsResourceWithRawResponse(self._pages.screenshots)

    @cached_property
    def contents(self) -> AsyncContentsResourceWithRawResponse:
        return AsyncContentsResourceWithRawResponse(self._pages.contents)


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.retrieve = to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            pages.list,
        )
        self.close = to_streamed_response_wrapper(
            pages.close,
        )
        self.do = to_streamed_response_wrapper(
            pages.do,
        )
        self.new_page = to_streamed_response_wrapper(
            pages.new_page,
        )
        self.step = to_streamed_response_wrapper(
            pages.step,
        )

    @cached_property
    def screenshots(self) -> ScreenshotsResourceWithStreamingResponse:
        return ScreenshotsResourceWithStreamingResponse(self._pages.screenshots)

    @cached_property
    def contents(self) -> ContentsResourceWithStreamingResponse:
        return ContentsResourceWithStreamingResponse(self._pages.contents)


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.retrieve = async_to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            pages.list,
        )
        self.close = async_to_streamed_response_wrapper(
            pages.close,
        )
        self.do = async_to_streamed_response_wrapper(
            pages.do,
        )
        self.new_page = async_to_streamed_response_wrapper(
            pages.new_page,
        )
        self.step = async_to_streamed_response_wrapper(
            pages.step,
        )

    @cached_property
    def screenshots(self) -> AsyncScreenshotsResourceWithStreamingResponse:
        return AsyncScreenshotsResourceWithStreamingResponse(self._pages.screenshots)

    @cached_property
    def contents(self) -> AsyncContentsResourceWithStreamingResponse:
        return AsyncContentsResourceWithStreamingResponse(self._pages.contents)
