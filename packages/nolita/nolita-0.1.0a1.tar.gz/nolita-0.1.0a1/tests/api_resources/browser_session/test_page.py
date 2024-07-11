# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nolita import Nolita, AsyncNolita
from tests.utils import assert_matches_type
from nolita.types.browser_session import PageGotoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_browse(self, client: Nolita) -> None:
        page = client.browser_session.page.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
        )
        assert_matches_type(object, page, path=["response"])

    @parametrize
    def test_method_browse_with_all_params(self, client: Nolita) -> None:
        page = client.browser_session.page.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
            inventory={
                "name": "YOUR NAME",
                "creditCard": "555555555555",
            },
            schema={},
        )
        assert_matches_type(object, page, path=["response"])

    @parametrize
    def test_raw_response_browse(self, client: Nolita) -> None:
        response = client.browser_session.page.with_raw_response.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(object, page, path=["response"])

    @parametrize
    def test_streaming_response_browse(self, client: Nolita) -> None:
        with client.browser_session.page.with_streaming_response.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_browse(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_session.page.with_raw_response.browse(
                "string",
                browser_session="",
                command="Find all the email addresses on the page",
                max_turns=20,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.browser_session.page.with_raw_response.browse(
                "",
                browser_session="string",
                command="Find all the email addresses on the page",
                max_turns=20,
            )

    @parametrize
    def test_method_goto(self, client: Nolita) -> None:
        page = client.browser_session.page.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )
        assert_matches_type(PageGotoResponse, page, path=["response"])

    @parametrize
    def test_method_goto_with_all_params(self, client: Nolita) -> None:
        page = client.browser_session.page.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
            headless=True,
            inventory=[
                {
                    "name": "Username",
                    "value": "tdaly",
                    "type": "string",
                },
                {
                    "name": "Username",
                    "value": "tdaly",
                    "type": "string",
                },
                {
                    "name": "Username",
                    "value": "tdaly",
                    "type": "string",
                },
            ],
            response_type={
                "type": "object",
                "properties": {
                    "numberOfActiveUsers": {
                        "type": "number",
                        "required": True,
                        "description": "The number of active users",
                    }
                },
            },
        )
        assert_matches_type(PageGotoResponse, page, path=["response"])

    @parametrize
    def test_raw_response_goto(self, client: Nolita) -> None:
        response = client.browser_session.page.with_raw_response.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageGotoResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_goto(self, client: Nolita) -> None:
        with client.browser_session.page.with_streaming_response.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageGotoResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_goto(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_session.page.with_raw_response.goto(
                "string",
                browser_session="",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.browser_session.page.with_raw_response.goto(
                "",
                browser_session="string",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )


class TestAsyncPage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_browse(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_session.page.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
        )
        assert_matches_type(object, page, path=["response"])

    @parametrize
    async def test_method_browse_with_all_params(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_session.page.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
            inventory={
                "name": "YOUR NAME",
                "creditCard": "555555555555",
            },
            schema={},
        )
        assert_matches_type(object, page, path=["response"])

    @parametrize
    async def test_raw_response_browse(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_session.page.with_raw_response.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(object, page, path=["response"])

    @parametrize
    async def test_streaming_response_browse(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_session.page.with_streaming_response.browse(
            "string",
            browser_session="string",
            command="Find all the email addresses on the page",
            max_turns=20,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(object, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_browse(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_session.page.with_raw_response.browse(
                "string",
                browser_session="",
                command="Find all the email addresses on the page",
                max_turns=20,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.browser_session.page.with_raw_response.browse(
                "",
                browser_session="string",
                command="Find all the email addresses on the page",
                max_turns=20,
            )

    @parametrize
    async def test_method_goto(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_session.page.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )
        assert_matches_type(PageGotoResponse, page, path=["response"])

    @parametrize
    async def test_method_goto_with_all_params(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_session.page.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
            headless=True,
            inventory=[
                {
                    "name": "Username",
                    "value": "tdaly",
                    "type": "string",
                },
                {
                    "name": "Username",
                    "value": "tdaly",
                    "type": "string",
                },
                {
                    "name": "Username",
                    "value": "tdaly",
                    "type": "string",
                },
            ],
            response_type={
                "type": "object",
                "properties": {
                    "numberOfActiveUsers": {
                        "type": "number",
                        "required": True,
                        "description": "The number of active users",
                    }
                },
            },
        )
        assert_matches_type(PageGotoResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_goto(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_session.page.with_raw_response.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageGotoResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_goto(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_session.page.with_streaming_response.goto(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageGotoResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_goto(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_session.page.with_raw_response.goto(
                "string",
                browser_session="",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.browser_session.page.with_raw_response.goto(
                "",
                browser_session="string",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )
