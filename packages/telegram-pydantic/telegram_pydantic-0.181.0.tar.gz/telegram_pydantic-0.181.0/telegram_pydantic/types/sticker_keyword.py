from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickerKeyword(BaseModel):
    """
    types.StickerKeyword
    ID: 0xfcfeb29c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StickerKeyword'] = pydantic.Field(
        'types.StickerKeyword',
        alias='_'
    )

    document_id: int
    keyword: list[str]
