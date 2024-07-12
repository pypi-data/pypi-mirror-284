from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsBots(BaseModel):
    """
    types.ChannelParticipantsBots
    ID: 0xb0d1865b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsBots'] = pydantic.Field(
        'types.ChannelParticipantsBots',
        alias='_'
    )

