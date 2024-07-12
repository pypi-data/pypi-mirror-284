from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateInlineBotCallbackQuery(BaseModel):
    """
    types.UpdateInlineBotCallbackQuery
    ID: 0x691e9052
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateInlineBotCallbackQuery'] = pydantic.Field(
        'types.UpdateInlineBotCallbackQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    msg_id: "base.InputBotInlineMessageID"
    chat_instance: int
    data: typing.Optional[bytes] = None
    game_short_name: typing.Optional[str] = None
