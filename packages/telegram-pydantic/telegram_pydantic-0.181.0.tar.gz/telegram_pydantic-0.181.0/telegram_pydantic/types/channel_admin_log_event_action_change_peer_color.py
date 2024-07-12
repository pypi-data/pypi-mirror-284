from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionChangePeerColor(BaseModel):
    """
    types.ChannelAdminLogEventActionChangePeerColor
    ID: 0x5796e780
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionChangePeerColor'] = pydantic.Field(
        'types.ChannelAdminLogEventActionChangePeerColor',
        alias='_'
    )

    prev_value: "base.PeerColor"
    new_value: "base.PeerColor"
