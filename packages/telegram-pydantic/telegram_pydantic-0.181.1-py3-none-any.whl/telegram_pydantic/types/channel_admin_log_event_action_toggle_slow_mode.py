from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleSlowMode(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleSlowMode
    ID: 0x53909779
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleSlowMode'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleSlowMode',
        alias='_'
    )

    prev_value: int
    new_value: int
