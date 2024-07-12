from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBusinessChatLink(BaseModel):
    """
    types.InputBusinessChatLink
    ID: 0x11679fa7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBusinessChatLink'] = pydantic.Field(
        'types.InputBusinessChatLink',
        alias='_'
    )

    message: str
    entities: typing.Optional[list["base.MessageEntity"]] = None
    title: typing.Optional[str] = None
