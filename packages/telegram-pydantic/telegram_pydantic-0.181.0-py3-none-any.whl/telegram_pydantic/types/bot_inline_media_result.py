from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInlineMediaResult(BaseModel):
    """
    types.BotInlineMediaResult
    ID: 0x17db940b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInlineMediaResult'] = pydantic.Field(
        'types.BotInlineMediaResult',
        alias='_'
    )

    id: str
    type: str
    send_message: "base.BotInlineMessage"
    photo: typing.Optional["base.Photo"] = None
    document: typing.Optional["base.Document"] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
