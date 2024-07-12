from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsAdmins(BaseModel):
    """
    types.ChannelParticipantsAdmins
    ID: 0xb4608969
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsAdmins'] = pydantic.Field(
        'types.ChannelParticipantsAdmins',
        alias='_'
    )

