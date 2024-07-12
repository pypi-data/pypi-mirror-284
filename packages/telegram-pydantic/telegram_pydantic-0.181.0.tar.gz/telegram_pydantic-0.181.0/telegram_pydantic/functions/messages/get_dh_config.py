from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDhConfig(BaseModel):
    """
    functions.messages.GetDhConfig
    ID: 0x26cf8950
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDhConfig'] = pydantic.Field(
        'functions.messages.GetDhConfig',
        alias='_'
    )

    version: int
    random_length: int
