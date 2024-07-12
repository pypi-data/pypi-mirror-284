from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangeProfilePeerColor(BaseModel):
    """
    types.ChannelAdminLogEventActionChangeProfilePeerColor
    ID: 0x5e477b25
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangeProfilePeerColor'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangeProfilePeerColor',
        alias='_'
    )

    prev_value: "base.PeerColor"
    new_value: "base.PeerColor"
