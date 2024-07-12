from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantJoin(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantJoin
    ID: 0x183040d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantJoin'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantJoin',
        alias='_'
    )

