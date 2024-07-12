from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleAntiSpam(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleAntiSpam
    ID: 0x64f36dfc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleAntiSpam'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleAntiSpam',
        alias='_'
    )

    new_value: bool
