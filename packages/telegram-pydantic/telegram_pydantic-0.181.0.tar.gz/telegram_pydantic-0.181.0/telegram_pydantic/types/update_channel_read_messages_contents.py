from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelReadMessagesContents(BaseModel):
    """
    types.UpdateChannelReadMessagesContents
    ID: 0xea29055d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelReadMessagesContents'] = pydantic.Field(
        'types.UpdateChannelReadMessagesContents',
        alias='_'
    )

    channel_id: int
    messages: list[int]
    top_msg_id: typing.Optional[int] = None
