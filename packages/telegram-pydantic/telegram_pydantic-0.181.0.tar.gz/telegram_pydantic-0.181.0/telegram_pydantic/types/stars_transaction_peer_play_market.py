from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransactionPeerPlayMarket(BaseModel):
    """
    types.StarsTransactionPeerPlayMarket
    ID: 0x7b560a0b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransactionPeerPlayMarket'] = pydantic.Field(
        'types.StarsTransactionPeerPlayMarket',
        alias='_'
    )

