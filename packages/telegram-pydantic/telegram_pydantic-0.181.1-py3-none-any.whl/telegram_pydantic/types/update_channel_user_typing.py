from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChannelUserTyping(BaseModel):
    """
    types.UpdateChannelUserTyping
    ID: 0x8c88c923
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChannelUserTyping'] = pydantic.Field(
        'types.UpdateChannelUserTyping',
        alias='_'
    )

    channel_id: int
    from_id: "base.Peer"
    action: "base.SendMessageAction"
    top_msg_id: typing.Optional[int] = None
