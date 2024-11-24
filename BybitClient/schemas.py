from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

# TODO дописать схемы респонсов


class ConvertStatuses(str, Enum):
    INIT = 'init'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    FAILURE = 'failure'

    def __str__(self) -> str:
        return self.value


class CoinLIstRequest(BaseModel):
    coin: Optional[str] = Field(description='Coin, uppercase only. Convert from coin (coin to sell)'
                                            'when side=0, coin field is ignored')

    side: 0 | 1 = Field(default=1, description='0: fromCoin list, the balance is given if you have it; '
                                               '1: toCoin list (coin to buy). When side=1 and coin field is filled, '
                                               'it returns toCoin list based on coin field')


class QuoteApplyRequest(BaseModel):
    from_coin: str = Field(..., alias='fromCoin', description='Convert from coin (coin to sell)')
    to_coin: str = Field(..., alias='toCoin', description='Convert to coin (coin to buy)')
    request_coin: str = Field(..., alias='requestCoin', description='Request coin, same as fromCoin')
    request_amount: str = Field(..., alias='requestAmount', description='request coin amount '
                                                                        '(the amount you want to sell)')


class QuoteConfirmStatusRequest(BaseModel):
    quote_tx_id: str = Field(..., alias='quoteTxId', description='Quote transaction ID from Request a Quote.'
                                                                 'It is system generated, and it is used to confirm '
                                                                 'quote and query the result of transaction')
