from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaDice(BaseModel):
    """
    types.InputMediaDice
    ID: 0xe66fbf7b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaDice'] = pydantic.Field(
        'types.InputMediaDice',
        alias='_'
    )

    emoticon: str
