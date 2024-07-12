from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAvailableEffects(BaseModel):
    """
    functions.messages.GetAvailableEffects
    ID: 0xdea20a39
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAvailableEffects'] = pydantic.Field(
        'functions.messages.GetAvailableEffects',
        alias='_'
    )

    hash: int
