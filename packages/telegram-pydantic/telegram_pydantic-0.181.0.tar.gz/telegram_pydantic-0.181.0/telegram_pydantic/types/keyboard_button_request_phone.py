from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonRequestPhone(BaseModel):
    """
    types.KeyboardButtonRequestPhone
    ID: 0xb16a6c29
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonRequestPhone'] = pydantic.Field(
        'types.KeyboardButtonRequestPhone',
        alias='_'
    )

    text: str
