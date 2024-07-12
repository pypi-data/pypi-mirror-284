from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyForumTopic(BaseModel):
    """
    types.InputNotifyForumTopic
    ID: 0x5c467992
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyForumTopic'] = pydantic.Field(
        'types.InputNotifyForumTopic',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: int
