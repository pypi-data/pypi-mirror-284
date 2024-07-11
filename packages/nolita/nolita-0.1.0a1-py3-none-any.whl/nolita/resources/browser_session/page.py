# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.browser_session import page_goto_params, page_browse_params
from ...types.browser_session.page_goto_response import PageGotoResponse

__all__ = ["PageResource", "AsyncPageResource"]


class PageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PageResourceWithRawResponse:
        return PageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PageResourceWithStreamingResponse:
        return PageResourceWithStreamingResponse(self)

    def browse(
        self,
        page_id: str,
        *,
        browser_session: str,
        command: str,
        max_turns: float,
        inventory: Dict[str, str] | NotGiven = NOT_GIVEN,
        schema: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            f"/{browser_session}/page/{page_id}/browse",
            body=maybe_transform(
                {
                    "command": command,
                    "max_turns": max_turns,
                    "inventory": inventory,
                    "schema": schema,
                },
                page_browse_params.PageBrowseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def goto(
        self,
        page_id: str,
        *,
        browser_session: str,
        browse_config: page_goto_params.BrowseConfig,
        headless: bool | NotGiven = NOT_GIVEN,
        inventory: Iterable[page_goto_params.Inventory] | NotGiven = NOT_GIVEN,
        response_type: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageGotoResponse:
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
            f"/{browser_session}/page/{page_id}/goto",
            body=maybe_transform(
                {
                    "browse_config": browse_config,
                    "headless": headless,
                    "inventory": inventory,
                    "response_type": response_type,
                },
                page_goto_params.PageGotoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageGotoResponse,
        )


class AsyncPageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPageResourceWithRawResponse:
        return AsyncPageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPageResourceWithStreamingResponse:
        return AsyncPageResourceWithStreamingResponse(self)

    async def browse(
        self,
        page_id: str,
        *,
        browser_session: str,
        command: str,
        max_turns: float,
        inventory: Dict[str, str] | NotGiven = NOT_GIVEN,
        schema: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            f"/{browser_session}/page/{page_id}/browse",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "max_turns": max_turns,
                    "inventory": inventory,
                    "schema": schema,
                },
                page_browse_params.PageBrowseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def goto(
        self,
        page_id: str,
        *,
        browser_session: str,
        browse_config: page_goto_params.BrowseConfig,
        headless: bool | NotGiven = NOT_GIVEN,
        inventory: Iterable[page_goto_params.Inventory] | NotGiven = NOT_GIVEN,
        response_type: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageGotoResponse:
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
            f"/{browser_session}/page/{page_id}/goto",
            body=await async_maybe_transform(
                {
                    "browse_config": browse_config,
                    "headless": headless,
                    "inventory": inventory,
                    "response_type": response_type,
                },
                page_goto_params.PageGotoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PageGotoResponse,
        )


class PageResourceWithRawResponse:
    def __init__(self, page: PageResource) -> None:
        self._page = page

        self.browse = to_raw_response_wrapper(
            page.browse,
        )
        self.goto = to_raw_response_wrapper(
            page.goto,
        )


class AsyncPageResourceWithRawResponse:
    def __init__(self, page: AsyncPageResource) -> None:
        self._page = page

        self.browse = async_to_raw_response_wrapper(
            page.browse,
        )
        self.goto = async_to_raw_response_wrapper(
            page.goto,
        )


class PageResourceWithStreamingResponse:
    def __init__(self, page: PageResource) -> None:
        self._page = page

        self.browse = to_streamed_response_wrapper(
            page.browse,
        )
        self.goto = to_streamed_response_wrapper(
            page.goto,
        )


class AsyncPageResourceWithStreamingResponse:
    def __init__(self, page: AsyncPageResource) -> None:
        self._page = page

        self.browse = async_to_streamed_response_wrapper(
            page.browse,
        )
        self.goto = async_to_streamed_response_wrapper(
            page.goto,
        )
