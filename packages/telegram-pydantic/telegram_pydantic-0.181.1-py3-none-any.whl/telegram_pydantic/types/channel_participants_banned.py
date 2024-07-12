from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsBanned(BaseModel):
    """
    types.ChannelParticipantsBanned
    ID: 0x1427a5e1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsBanned'] = pydantic.Field(
        'types.ChannelParticipantsBanned',
        alias='_'
    )

    q: str
