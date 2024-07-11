# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nolita import Nolita, AsyncNolita
from tests.utils import assert_matches_type
from nolita.types.browser_sessions import (
    PageDoResponse,
    PageListResponse,
    PageStepResponse,
    PageCloseResponse,
    PageNewPageResponse,
    PageRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.retrieve(
            "string",
            browser_session="string",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Nolita) -> None:
        response = client.browser_sessions.pages.with_raw_response.retrieve(
            "string",
            browser_session="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Nolita) -> None:
        with client.browser_sessions.pages.with_streaming_response.retrieve(
            "string",
            browser_session="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_sessions.pages.with_raw_response.retrieve(
                "string",
                browser_session="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.browser_sessions.pages.with_raw_response.retrieve(
                "",
                browser_session="string",
            )

    @parametrize
    def test_method_list(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.list(
            "string",
        )
        assert_matches_type(PageListResponse, page, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Nolita) -> None:
        response = client.browser_sessions.pages.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageListResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Nolita) -> None:
        with client.browser_sessions.pages.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageListResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_sessions.pages.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_close(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.close(
            "string",
            browser_session="string",
        )
        assert_matches_type(PageCloseResponse, page, path=["response"])

    @parametrize
    def test_raw_response_close(self, client: Nolita) -> None:
        response = client.browser_sessions.pages.with_raw_response.close(
            "string",
            browser_session="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageCloseResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_close(self, client: Nolita) -> None:
        with client.browser_sessions.pages.with_streaming_response.close(
            "string",
            browser_session="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageCloseResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_sessions.pages.with_raw_response.close(
                "string",
                browser_session="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.browser_sessions.pages.with_raw_response.close(
                "",
                browser_session="string",
            )

    @parametrize
    def test_method_do(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.do(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )
        assert_matches_type(PageDoResponse, page, path=["response"])

    @parametrize
    def test_method_do_with_all_params(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.do(
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
        assert_matches_type(PageDoResponse, page, path=["response"])

    @parametrize
    def test_raw_response_do(self, client: Nolita) -> None:
        response = client.browser_sessions.pages.with_raw_response.do(
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
        assert_matches_type(PageDoResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_do(self, client: Nolita) -> None:
        with client.browser_sessions.pages.with_streaming_response.do(
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
            assert_matches_type(PageDoResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_do(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_sessions.pages.with_raw_response.do(
                "string",
                browser_session="",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.browser_sessions.pages.with_raw_response.do(
                "",
                browser_session="string",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )

    @parametrize
    def test_method_new_page(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.new_page(
            "string",
        )
        assert_matches_type(PageNewPageResponse, page, path=["response"])

    @parametrize
    def test_raw_response_new_page(self, client: Nolita) -> None:
        response = client.browser_sessions.pages.with_raw_response.new_page(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageNewPageResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_new_page(self, client: Nolita) -> None:
        with client.browser_sessions.pages.with_streaming_response.new_page(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageNewPageResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_new_page(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_sessions.pages.with_raw_response.new_page(
                "",
            )

    @parametrize
    def test_method_step(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.step(
            "string",
            browser_session="string",
            command="Click on the login button",
        )
        assert_matches_type(PageStepResponse, page, path=["response"])

    @parametrize
    def test_method_step_with_all_params(self, client: Nolita) -> None:
        page = client.browser_sessions.pages.step(
            "string",
            browser_session="string",
            command="Click on the login button",
            opts={
                "delay": 100,
                "inventory": {
                    "name": "YOUR NAME",
                    "creditCard": "555555555555",
                },
            },
            schema={},
        )
        assert_matches_type(PageStepResponse, page, path=["response"])

    @parametrize
    def test_raw_response_step(self, client: Nolita) -> None:
        response = client.browser_sessions.pages.with_raw_response.step(
            "string",
            browser_session="string",
            command="Click on the login button",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageStepResponse, page, path=["response"])

    @parametrize
    def test_streaming_response_step(self, client: Nolita) -> None:
        with client.browser_sessions.pages.with_streaming_response.step(
            "string",
            browser_session="string",
            command="Click on the login button",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageStepResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_step(self, client: Nolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            client.browser_sessions.pages.with_raw_response.step(
                "string",
                browser_session="",
                command="Click on the login button",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            client.browser_sessions.pages.with_raw_response.step(
                "",
                browser_session="string",
                command="Click on the login button",
            )


class TestAsyncPages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.retrieve(
            "string",
            browser_session="string",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_sessions.pages.with_raw_response.retrieve(
            "string",
            browser_session="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_sessions.pages.with_streaming_response.retrieve(
            "string",
            browser_session="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.retrieve(
                "string",
                browser_session="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.retrieve(
                "",
                browser_session="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.list(
            "string",
        )
        assert_matches_type(PageListResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_sessions.pages.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageListResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_sessions.pages.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageListResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_close(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.close(
            "string",
            browser_session="string",
        )
        assert_matches_type(PageCloseResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_sessions.pages.with_raw_response.close(
            "string",
            browser_session="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageCloseResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_sessions.pages.with_streaming_response.close(
            "string",
            browser_session="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageCloseResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.close(
                "string",
                browser_session="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.close(
                "",
                browser_session="string",
            )

    @parametrize
    async def test_method_do(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.do(
            "string",
            browser_session="string",
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )
        assert_matches_type(PageDoResponse, page, path=["response"])

    @parametrize
    async def test_method_do_with_all_params(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.do(
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
        assert_matches_type(PageDoResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_do(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_sessions.pages.with_raw_response.do(
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
        assert_matches_type(PageDoResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_do(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_sessions.pages.with_streaming_response.do(
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
            assert_matches_type(PageDoResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_do(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.do(
                "string",
                browser_session="",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.do(
                "",
                browser_session="string",
                browse_config={
                    "start_url": "https://google.com",
                    "objective": ["what is the most active game on steam and what is the number of users?"],
                    "max_iterations": 10,
                },
            )

    @parametrize
    async def test_method_new_page(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.new_page(
            "string",
        )
        assert_matches_type(PageNewPageResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_new_page(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_sessions.pages.with_raw_response.new_page(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageNewPageResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_new_page(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_sessions.pages.with_streaming_response.new_page(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageNewPageResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_new_page(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.new_page(
                "",
            )

    @parametrize
    async def test_method_step(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.step(
            "string",
            browser_session="string",
            command="Click on the login button",
        )
        assert_matches_type(PageStepResponse, page, path=["response"])

    @parametrize
    async def test_method_step_with_all_params(self, async_client: AsyncNolita) -> None:
        page = await async_client.browser_sessions.pages.step(
            "string",
            browser_session="string",
            command="Click on the login button",
            opts={
                "delay": 100,
                "inventory": {
                    "name": "YOUR NAME",
                    "creditCard": "555555555555",
                },
            },
            schema={},
        )
        assert_matches_type(PageStepResponse, page, path=["response"])

    @parametrize
    async def test_raw_response_step(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser_sessions.pages.with_raw_response.step(
            "string",
            browser_session="string",
            command="Click on the login button",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageStepResponse, page, path=["response"])

    @parametrize
    async def test_streaming_response_step(self, async_client: AsyncNolita) -> None:
        async with async_client.browser_sessions.pages.with_streaming_response.step(
            "string",
            browser_session="string",
            command="Click on the login button",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageStepResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_step(self, async_client: AsyncNolita) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `browser_session` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.step(
                "string",
                browser_session="",
                command="Click on the login button",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `page_id` but received ''"):
            await async_client.browser_sessions.pages.with_raw_response.step(
                "",
                browser_session="string",
                command="Click on the login button",
            )
