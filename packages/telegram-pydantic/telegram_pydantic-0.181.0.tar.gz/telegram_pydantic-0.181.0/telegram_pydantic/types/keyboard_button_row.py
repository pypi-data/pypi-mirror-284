from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonRow(BaseModel):
    """
    types.KeyboardButtonRow
    ID: 0x77608b83
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonRow'] = pydantic.Field(
        'types.KeyboardButtonRow',
        alias='_'
    )

    buttons: list["base.KeyboardButton"]
