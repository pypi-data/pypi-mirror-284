from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetInlineGameScore(BaseModel):
    """
    functions.messages.SetInlineGameScore
    ID: 0x15ad9f64
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetInlineGameScore'] = pydantic.Field(
        'functions.messages.SetInlineGameScore',
        alias='_'
    )

    id: "base.InputBotInlineMessageID"
    user_id: "base.InputUser"
    score: int
    edit_message: typing.Optional[bool] = None
    force: typing.Optional[bool] = None
