# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nolita import Nolita, AsyncNolita
from tests.utils import assert_matches_type
from nolita.types import BrowserSessionCloseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowserSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_close(self, client: Nolita) -> None:
        browser_session = client.browser_session.close(
            "string",
        )
        assert_matches_type(BrowserSessionCloseResponse, browser_session, path=["response"])

    @parametrize
    def test_raw_response_close(self, client: Nolita) -> None:
        response = client.browser_session.with_raw_response.close(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = response.parse()
        assert_matches_type(BrowserSessionCloseResponse, browser_session, path=["response"])

    @parametrize
    def test_streaming_response_close(self, client: Nolita) -> None:
        with client.browser_session.with_streaming_response.close(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = response.parse()
            assert_matches_type(BrowserSessionCloseResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_session.with_raw_response.close(
                "",
            )


class TestAsyncBrowserSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_close(self, async_client: AsyncNolita) -> None:
        browser_session = await async_client.browser_session.close(
            "string",
        )
        assert_matches_type(BrowserSessionCloseResponse, browser_session, path=["response"])

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_session.with_raw_response.close(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = await response.parse()
        assert_matches_type(BrowserSessionCloseResponse, browser_session, path=["response"])

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_session.with_streaming_response.close(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = await response.parse()
            assert_matches_type(BrowserSessionCloseResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_session.with_raw_response.close(
                "",
            )
