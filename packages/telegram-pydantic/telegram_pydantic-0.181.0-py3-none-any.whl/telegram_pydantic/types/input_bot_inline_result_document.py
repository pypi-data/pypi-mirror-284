from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotInlineResultDocument(BaseModel):
    """
    types.InputBotInlineResultDocument
    ID: 0xfff8fdc4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotInlineResultDocument'] = pydantic.Field(
        'types.InputBotInlineResultDocument',
        alias='_'
    )

    id: str
    type: str
    document: "base.InputDocument"
    send_message: "base.InputBotInlineMessage"
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
