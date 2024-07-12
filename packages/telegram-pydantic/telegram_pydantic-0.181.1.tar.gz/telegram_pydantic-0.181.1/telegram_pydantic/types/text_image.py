from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextImage(BaseModel):
    """
    types.TextImage
    ID: 0x81ccf4f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextImage'] = pydantic.Field(
        'types.TextImage',
        alias='_'
    )

    document_id: int
    w: int
    h: int
