from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonBuy(BaseModel):
    """
    types.KeyboardButtonBuy
    ID: 0xafd93fbb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonBuy'] = pydantic.Field(
        'types.KeyboardButtonBuy',
        alias='_'
    )

    text: str
