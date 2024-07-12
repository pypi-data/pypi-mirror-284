from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeHasStickers(BaseModel):
    """
    types.DocumentAttributeHasStickers
    ID: 0x9801d2f7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeHasStickers'] = pydantic.Field(
        'types.DocumentAttributeHasStickers',
        alias='_'
    )

