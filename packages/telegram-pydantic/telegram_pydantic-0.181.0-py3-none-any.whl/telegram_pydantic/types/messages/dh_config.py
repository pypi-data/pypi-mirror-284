from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DhConfig(BaseModel):
    """
    types.messages.DhConfig
    ID: 0x2c221edd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DhConfig'] = pydantic.Field(
        'types.messages.DhConfig',
        alias='_'
    )

    g: int
    p: bytes
    version: int
    random: bytes
