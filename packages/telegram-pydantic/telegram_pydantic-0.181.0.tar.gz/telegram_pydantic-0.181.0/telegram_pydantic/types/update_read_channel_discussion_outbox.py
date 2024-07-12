from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadChannelDiscussionOutbox(BaseModel):
    """
    types.UpdateReadChannelDiscussionOutbox
    ID: 0x695c9e7c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadChannelDiscussionOutbox'] = pydantic.Field(
        'types.UpdateReadChannelDiscussionOutbox',
        alias='_'
    )

    channel_id: int
    top_msg_id: int
    read_max_id: int
