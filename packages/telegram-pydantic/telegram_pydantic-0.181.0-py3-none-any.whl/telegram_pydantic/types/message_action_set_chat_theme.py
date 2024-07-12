from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionSetChatTheme(BaseModel):
    """
    types.MessageActionSetChatTheme
    ID: 0xaa786345
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionSetChatTheme'] = pydantic.Field(
        'types.MessageActionSetChatTheme',
        alias='_'
    )

    emoticon: str
