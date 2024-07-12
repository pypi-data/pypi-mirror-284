from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeEmojiStatus(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeEmojiStatus
    ID: 0x3ea9feb1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeEmojiStatus'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeEmojiStatus',
        alias='_'
    )

    prev_value: "base.EmojiStatus"
    new_value: "base.EmojiStatus"
