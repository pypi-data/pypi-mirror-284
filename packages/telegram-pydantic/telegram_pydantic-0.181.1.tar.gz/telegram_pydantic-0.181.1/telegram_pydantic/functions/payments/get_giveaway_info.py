from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGiveawayInfo(BaseModel):
    """
    functions.payments.GetGiveawayInfo
    ID: 0xf4239425
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetGiveawayInfo'] = pydantic.Field(
        'functions.payments.GetGiveawayInfo',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
