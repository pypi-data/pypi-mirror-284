# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.trading.execution_report import ExecutionReport
from ...types.trading.quote_execution_report import QuoteExecutionReport

__all__ = ["ExecutionReportResource", "AsyncExecutionReportResource"]


class ExecutionReportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecutionReportResourceWithRawResponse:
        return ExecutionReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionReportResourceWithStreamingResponse:
        return ExecutionReportResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionReport:
        """Quote will give the best quote from all available exchange accounts"""
        return self._get(
            "/api/v2/trading/listExecutionReports",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionReport,
        )

    def get_quote_execution_report(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuoteExecutionReport:
        """Quote will give the best quote from all available exchange accounts"""
        return self._get(
            "/api/v2/trading/getQuoteExecutionReport",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteExecutionReport,
        )


class AsyncExecutionReportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecutionReportResourceWithRawResponse:
        return AsyncExecutionReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionReportResourceWithStreamingResponse:
        return AsyncExecutionReportResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecutionReport:
        """Quote will give the best quote from all available exchange accounts"""
        return await self._get(
            "/api/v2/trading/listExecutionReports",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionReport,
        )

    async def get_quote_execution_report(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuoteExecutionReport:
        """Quote will give the best quote from all available exchange accounts"""
        return await self._get(
            "/api/v2/trading/getQuoteExecutionReport",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteExecutionReport,
        )


class ExecutionReportResourceWithRawResponse:
    def __init__(self, execution_report: ExecutionReportResource) -> None:
        self._execution_report = execution_report

        self.list = to_raw_response_wrapper(
            execution_report.list,
        )
        self.get_quote_execution_report = to_raw_response_wrapper(
            execution_report.get_quote_execution_report,
        )


class AsyncExecutionReportResourceWithRawResponse:
    def __init__(self, execution_report: AsyncExecutionReportResource) -> None:
        self._execution_report = execution_report

        self.list = async_to_raw_response_wrapper(
            execution_report.list,
        )
        self.get_quote_execution_report = async_to_raw_response_wrapper(
            execution_report.get_quote_execution_report,
        )


class ExecutionReportResourceWithStreamingResponse:
    def __init__(self, execution_report: ExecutionReportResource) -> None:
        self._execution_report = execution_report

        self.list = to_streamed_response_wrapper(
            execution_report.list,
        )
        self.get_quote_execution_report = to_streamed_response_wrapper(
            execution_report.get_quote_execution_report,
        )


class AsyncExecutionReportResourceWithStreamingResponse:
    def __init__(self, execution_report: AsyncExecutionReportResource) -> None:
        self._execution_report = execution_report

        self.list = async_to_streamed_response_wrapper(
            execution_report.list,
        )
        self.get_quote_execution_report = async_to_streamed_response_wrapper(
            execution_report.get_quote_execution_report,
        )
