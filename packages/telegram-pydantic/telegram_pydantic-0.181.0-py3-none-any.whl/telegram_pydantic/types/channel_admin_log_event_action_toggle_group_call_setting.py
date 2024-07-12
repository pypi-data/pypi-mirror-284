from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleGroupCallSetting(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleGroupCallSetting
    ID: 0x56d6a247
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleGroupCallSetting'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleGroupCallSetting',
        alias='_'
    )

    join_muted: bool
