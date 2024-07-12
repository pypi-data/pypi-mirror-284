from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionParticipantLeave(BaseModel):
    """
    types.ChannelAdminLogEventActionParticipantLeave
    ID: 0xf89777f2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionParticipantLeave'] = pydantic.Field(
        'types.ChannelAdminLogEventActionParticipantLeave',
        alias='_'
    )

