from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeImageSize(BaseModel):
    """
    types.DocumentAttributeImageSize
    ID: 0x6c37c15c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeImageSize'] = pydantic.Field(
        'types.DocumentAttributeImageSize',
        alias='_'
    )

    w: int
    h: int
