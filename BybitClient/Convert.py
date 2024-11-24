from enum import Enum
from time import sleep

from pybit._http_manager import _V5HTTPManager

from .exceptions import MaxRetryStatusException
from .schemas import (CoinLIstRequest, ConvertStatuses, QuoteApplyRequest,
                      QuoteConfirmStatusRequest)

DONE_STATUSES = [ConvertStatuses.SUCCESS, ConvertStatuses.FAILURE]


class Convert(str, Enum):
    GET_CONVERT_COIN_LIST = '/v5/asset/exchange/query-coin-list'
    POST_QOUTE_APPLY = '/v5/asset/exchange/quote-apply'
    POST_QUOTE_CONFIRM = '/v5/asset/exchange/convert-execute'
    GET_CONVERT_STATUS = '/v5/asset/exchange/convert-result-query'
    GET_CONVERT_HISTORY = '/v5/asset/exchange/convert-result-query'

    def __str__(self) -> str:
        return self.value


class ConvertHTTP(_V5HTTPManager):
    def get_convert_coin_list(self, params_query: CoinLIstRequest):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Convert.GET_CONVERT_COIN_LIST}",
            query=params_query.dict(by_alias=True, exclude_none=True),
            auth=True,
        )

    def quote_apply(self, params_query: QuoteApplyRequest):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Convert.POST_QOUTE_APPLY}",
            query=params_query.dict(by_alias=True, exclude_none=True),
            auth=True,
        )

    def _quote_confirm(self, params_query: QuoteConfirmStatusRequest):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Convert.POST_QUOTE_CONFIRM}",
            query=params_query.dict(by_alias=True, exclude_none=True),
            auth=True,
        )

    def _convert_status(self, params_query: QuoteConfirmStatusRequest):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Convert.GET_CONVERT_STATUS}",
            query=params_query.dict(by_alias=True, exclude_none=True),
            auth=True,
        )

    def convert_coin(self, params_query: QuoteConfirmStatusRequest):
        result = self._quote_confirm(params_query)

        retry_count = 0
        max_retries = 100

        while result.exchange_status not in DONE_STATUSES:
            retry_count += 1
            result = self._convert_status(params_query)
            if retry_count >= max_retries:
                raise MaxRetryStatusException()
            sleep(0.5)

        return result
