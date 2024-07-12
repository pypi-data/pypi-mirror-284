from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StarsTransactionPeerPremiumBot(BaseModel):
    """
    types.StarsTransactionPeerPremiumBot
    ID: 0x250dbaf8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StarsTransactionPeerPremiumBot'] = pydantic.Field(
        'types.StarsTransactionPeerPremiumBot',
        alias='_'
    )

