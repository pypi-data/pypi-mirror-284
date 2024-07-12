from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateBotCallbackQuery(BaseModel):
    """
    types.UpdateBotCallbackQuery
    ID: 0xb9cfc48d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateBotCallbackQuery'] = pydantic.Field(
        'types.UpdateBotCallbackQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    peer: "base.Peer"
    msg_id: int
    chat_instance: int
    data: typing.Optional[bytes] = None
    game_short_name: typing.Optional[str] = None
