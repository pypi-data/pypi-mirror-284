from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetShortName(BaseModel):
    """
    types.InputStickerSetShortName
    ID: 0x861cc8a0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetShortName'] = pydantic.Field(
        'types.InputStickerSetShortName',
        alias='_'
    )

    short_name: str
