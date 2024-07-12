from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatEditTitle(BaseModel):
    """
    types.MessageActionChatEditTitle
    ID: 0xb5a1ce5a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatEditTitle'] = pydantic.Field(
        'types.MessageActionChatEditTitle',
        alias='_'
    )

    title: str
