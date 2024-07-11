# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import browse_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.objective_complete import ObjectiveComplete

__all__ = ["BrowseResource", "AsyncBrowseResource"]


class BrowseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrowseResourceWithRawResponse:
        return BrowseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowseResourceWithStreamingResponse:
        return BrowseResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        browse_config: browse_create_params.BrowseConfig,
        headless: bool | NotGiven = NOT_GIVEN,
        inventory: Iterable[browse_create_params.Inventory] | NotGiven = NOT_GIVEN,
        response_type: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectiveComplete:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/browse",
            body=maybe_transform(
                {
                    "browse_config": browse_config,
                    "headless": headless,
                    "inventory": inventory,
                    "response_type": response_type,
                },
                browse_create_params.BrowseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveComplete,
        )


class AsyncBrowseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrowseResourceWithRawResponse:
        return AsyncBrowseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowseResourceWithStreamingResponse:
        return AsyncBrowseResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        browse_config: browse_create_params.BrowseConfig,
        headless: bool | NotGiven = NOT_GIVEN,
        inventory: Iterable[browse_create_params.Inventory] | NotGiven = NOT_GIVEN,
        response_type: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectiveComplete:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/browse",
            body=await async_maybe_transform(
                {
                    "browse_config": browse_config,
                    "headless": headless,
                    "inventory": inventory,
                    "response_type": response_type,
                },
                browse_create_params.BrowseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveComplete,
        )


class BrowseResourceWithRawResponse:
    def __init__(self, browse: BrowseResource) -> None:
        self._browse = browse

        self.create = to_raw_response_wrapper(
            browse.create,
        )


class AsyncBrowseResourceWithRawResponse:
    def __init__(self, browse: AsyncBrowseResource) -> None:
        self._browse = browse

        self.create = async_to_raw_response_wrapper(
            browse.create,
        )


class BrowseResourceWithStreamingResponse:
    def __init__(self, browse: BrowseResource) -> None:
        self._browse = browse

        self.create = to_streamed_response_wrapper(
            browse.create,
        )


class AsyncBrowseResourceWithStreamingResponse:
    def __init__(self, browse: AsyncBrowseResource) -> None:
        self._browse = browse

        self.create = async_to_streamed_response_wrapper(
            browse.create,
        )
