from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class NotifyForumTopic(BaseModel):
    """
    types.NotifyForumTopic
    ID: 0x226e6308
    Layer: 181
    """
    QUALNAME: typing.Literal['types.NotifyForumTopic'] = pydantic.Field(
        'types.NotifyForumTopic',
        alias='_'
    )

    peer: "base.Peer"
    top_msg_id: int
