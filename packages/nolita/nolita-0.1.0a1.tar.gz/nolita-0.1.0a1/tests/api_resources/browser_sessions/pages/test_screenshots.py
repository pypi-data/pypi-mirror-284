# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nolita import Nolita, AsyncNolita
from tests.utils import assert_matches_type
from nolita.types.browser_sessions.pages import ScreenshotRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreenshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Nolita) -> None:
        screenshot = client.browser_sessions.pages.screenshots.retrieve(
            "base64",
            browser_session="string",
            page_id="string",
        )
        assert_matches_type(ScreenshotRetrieveResponse, screenshot, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Nolita) -> None:
        response = client.browser_sessions.pages.screenshots.with_raw_response.retrieve(
            "base64",
            browser_session="string",
            page_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = response.parse()
        assert_matches_type(ScreenshotRetrieveResponse, screenshot, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Nolita) -> None:
        with client.browser_sessions.pages.screenshots.with_streaming_response.retrieve(
            "base64",
            browser_session="string",
            page_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = response.parse()
            assert_matches_type(ScreenshotRetrieveResponse, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_sessions.pages.screenshots.with_raw_response.retrieve(
                "base64",
                browser_session="",
                page_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.browser_sessions.pages.screenshots.with_raw_response.retrieve(
                "base64",
                browser_session="string",
                page_id="",
            )


class TestAsyncScreenshots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNolita) -> None:
        screenshot = await async_client.browser_sessions.pages.screenshots.retrieve(
            "base64",
            browser_session="string",
            page_id="string",
        )
        assert_matches_type(ScreenshotRetrieveResponse, screenshot, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_sessions.pages.screenshots.with_raw_response.retrieve(
            "base64",
            browser_session="string",
            page_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screenshot = await response.parse()
        assert_matches_type(ScreenshotRetrieveResponse, screenshot, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_sessions.pages.screenshots.with_streaming_response.retrieve(
            "base64",
            browser_session="string",
            page_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screenshot = await response.parse()
            assert_matches_type(ScreenshotRetrieveResponse, screenshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_sessions.pages.screenshots.with_raw_response.retrieve(
                "base64",
                browser_session="",
                page_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.browser_sessions.pages.screenshots.with_raw_response.retrieve(
                "base64",
                browser_session="string",
                page_id="",
            )
