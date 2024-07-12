from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaEmpty(BaseModel):
    """
    types.MessageMediaEmpty
    ID: 0x3ded6320
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaEmpty'] = pydantic.Field(
        'types.MessageMediaEmpty',
        alias='_'
    )

