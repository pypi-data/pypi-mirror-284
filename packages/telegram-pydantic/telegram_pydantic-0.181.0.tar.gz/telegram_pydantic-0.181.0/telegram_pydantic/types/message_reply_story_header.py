from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageReplyStoryHeader(BaseModel):
    """
    types.MessageReplyStoryHeader
    ID: 0xe5af939
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageReplyStoryHeader'] = pydantic.Field(
        'types.MessageReplyStoryHeader',
        alias='_'
    )

    peer: "base.Peer"
    story_id: int
