from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetDice(BaseModel):
    """
    types.InputStickerSetDice
    ID: 0xe67f520e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetDice'] = pydantic.Field(
        'types.InputStickerSetDice',
        alias='_'
    )

    emoticon: str
