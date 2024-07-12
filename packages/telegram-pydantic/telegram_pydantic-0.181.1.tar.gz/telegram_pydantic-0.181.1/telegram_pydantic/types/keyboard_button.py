from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButton(BaseModel):
    """
    types.KeyboardButton
    ID: 0xa2fa4880
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButton'] = pydantic.Field(
        'types.KeyboardButton',
        alias='_'
    )

    text: str
