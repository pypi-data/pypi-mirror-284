from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionTopicCreate(BaseModel):
    """
    types.MessageActionTopicCreate
    ID: 0xd999256
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionTopicCreate'] = pydantic.Field(
        'types.MessageActionTopicCreate',
        alias='_'
    )

    title: str
    icon_color: int
    icon_emoji_id: typing.Optional[int] = None
