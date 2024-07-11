# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from nolita import Nolita, AsyncNolita
from tests.utils import assert_matches_type
from nolita.types.browser import SessionLaunchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_launch(self, client: Nolita) -> None:
        session = client.browser.session.launch(
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )
        assert_matches_type(SessionLaunchResponse, session, path=["response"])

    @parametrize
    def test_method_launch_with_all_params(self, client: Nolita) -> None:
        session = client.browser.session.launch(
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
        assert_matches_type(SessionLaunchResponse, session, path=["response"])

    @parametrize
    def test_raw_response_launch(self, client: Nolita) -> None:
        response = client.browser.session.with_raw_response.launch(
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionLaunchResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_launch(self, client: Nolita) -> None:
        with client.browser.session.with_streaming_response.launch(
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionLaunchResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_launch(self, async_client: AsyncNolita) -> None:
        session = await async_client.browser.session.launch(
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )
        assert_matches_type(SessionLaunchResponse, session, path=["response"])

    @parametrize
    async def test_method_launch_with_all_params(self, async_client: AsyncNolita) -> None:
        session = await async_client.browser.session.launch(
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
        assert_matches_type(SessionLaunchResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_launch(self, async_client: AsyncNolita) -> None:
        response = await async_client.browser.session.with_raw_response.launch(
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionLaunchResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_launch(self, async_client: AsyncNolita) -> None:
        async with async_client.browser.session.with_streaming_response.launch(
            browse_config={
                "start_url": "https://google.com",
                "objective": ["what is the most active game on steam and what is the number of users?"],
                "max_iterations": 10,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionLaunchResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True
