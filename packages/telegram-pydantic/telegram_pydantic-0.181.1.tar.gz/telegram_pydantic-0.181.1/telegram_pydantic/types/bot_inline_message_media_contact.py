from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMessageMediaContact(BaseModel):
    """
    types.BotInlineMessageMediaContact
    ID: 0x18d1cdc2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMessageMediaContact'] = pydantic.Field(
        'types.BotInlineMessageMediaContact',
        alias='_'
    )

    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    reply_markup: typing.Optional["base.ReplyMarkup"] = None
