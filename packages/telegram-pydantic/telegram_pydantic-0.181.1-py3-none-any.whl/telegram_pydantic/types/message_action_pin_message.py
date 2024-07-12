from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionPinMessage(BaseModel):
    """
    types.MessageActionPinMessage
    ID: 0x94bd38ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionPinMessage'] = pydantic.Field(
        'types.MessageActionPinMessage',
        alias='_'
    )

