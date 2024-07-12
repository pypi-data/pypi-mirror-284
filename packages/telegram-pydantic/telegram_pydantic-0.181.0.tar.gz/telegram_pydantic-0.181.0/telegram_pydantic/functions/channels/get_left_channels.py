from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLeftChannels(BaseModel):
    """
    functions.channels.GetLeftChannels
    ID: 0x8341ecc0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetLeftChannels'] = pydantic.Field(
        'functions.channels.GetLeftChannels',
        alias='_'
    )

    offset: int
