from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionStartGroupCall(BaseModel):
    """
    types.ChannelAdminLogEventActionStartGroupCall
    ID: 0x23209745
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionStartGroupCall'] = pydantic.Field(
        'types.ChannelAdminLogEventActionStartGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
