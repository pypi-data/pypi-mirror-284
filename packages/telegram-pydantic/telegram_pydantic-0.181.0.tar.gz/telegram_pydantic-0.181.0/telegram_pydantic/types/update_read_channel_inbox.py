from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadChannelInbox(BaseModel):
    """
    types.UpdateReadChannelInbox
    ID: 0x922e6e10
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadChannelInbox'] = pydantic.Field(
        'types.UpdateReadChannelInbox',
        alias='_'
    )

    channel_id: int
    max_id: int
    still_unread_count: int
    pts: int
    folder_id: typing.Optional[int] = None
