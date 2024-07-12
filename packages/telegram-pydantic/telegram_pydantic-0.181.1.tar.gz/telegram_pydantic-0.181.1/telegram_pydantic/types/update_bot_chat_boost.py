from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotChatBoost(BaseModel):
    """
    types.UpdateBotChatBoost
    ID: 0x904dd49c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotChatBoost'] = pydantic.Field(
        'types.UpdateBotChatBoost',
        alias='_'
    )

    peer: "base.Peer"
    boost: "base.Boost"
    qts: int
