from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionToggleInvites(BaseModel):
    """
    types.ChannelAdminLogEventActionToggleInvites
    ID: 0x1b7907ae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionToggleInvites'] = pydantic.Field(
        'types.ChannelAdminLogEventActionToggleInvites',
        alias='_'
    )

    new_value: bool
