from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmpty(BaseModel):
    """
    types.InputStickerSetEmpty
    ID: 0xffb62b95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmpty'] = pydantic.Field(
        'types.InputStickerSetEmpty',
        alias='_'
    )

