from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineMessageText(BaseModel):
    """
    types.InputBotInlineMessageText
    ID: 0x3dcd7a87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineMessageText'] = pydantic.Field(
        'types.InputBotInlineMessageText',
        alias='_'
    )

    message: str
    no_webpage: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
