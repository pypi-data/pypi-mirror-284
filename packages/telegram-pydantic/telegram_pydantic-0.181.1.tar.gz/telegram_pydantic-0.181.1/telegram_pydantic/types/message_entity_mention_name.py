from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityMentionName(BaseModel):
    """
    types.MessageEntityMentionName
    ID: 0xdc7b1140
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityMentionName'] = pydantic.Field(
        'types.MessageEntityMentionName',
        alias='_'
    )

    offset: int
    length: int
    user_id: int
