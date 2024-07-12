from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGiveawayLaunch(BaseModel):
    """
    types.MessageActionGiveawayLaunch
    ID: 0x332ba9ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGiveawayLaunch'] = pydantic.Field(
        'types.MessageActionGiveawayLaunch',
        alias='_'
    )

