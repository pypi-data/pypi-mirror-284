from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionChatJoinedByRequest(BaseModel):
    """
    types.MessageActionChatJoinedByRequest
    ID: 0xebbca3cb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionChatJoinedByRequest'] = pydantic.Field(
        'types.MessageActionChatJoinedByRequest',
        alias='_'
    )

