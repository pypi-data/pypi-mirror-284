from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineResultPhoto(BaseModel):
    """
    types.InputBotInlineResultPhoto
    ID: 0xa8d864a7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineResultPhoto'] = pydantic.Field(
        'types.InputBotInlineResultPhoto',
        alias='_'
    )

    id: str
    type: str
    photo: "base.InputPhoto"
    send_message: "base.InputBotInlineMessage"
