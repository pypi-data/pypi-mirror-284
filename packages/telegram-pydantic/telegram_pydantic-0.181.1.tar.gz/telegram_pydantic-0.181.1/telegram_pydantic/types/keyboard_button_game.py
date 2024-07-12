from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonGame(BaseModel):
    """
    types.KeyboardButtonGame
    ID: 0x50f41ccf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonGame'] = pydantic.Field(
        'types.KeyboardButtonGame',
        alias='_'
    )

    text: str
