from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditInlineBotMessage(BaseModel):
    """
    functions.messages.EditInlineBotMessage
    ID: 0x83557dba
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditInlineBotMessage'] = pydantic.Field(
        'functions.messages.EditInlineBotMessage',
        alias='_'
    )

    id: "base.InputBotInlineMessageID"
    no_webpage: typing.Optional[bool] = None
    invert_media: typing.Optional[bool] = None
    message: typing.Optional[str] = None
    media: typing.Optional["base.InputMedia"] = None
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
