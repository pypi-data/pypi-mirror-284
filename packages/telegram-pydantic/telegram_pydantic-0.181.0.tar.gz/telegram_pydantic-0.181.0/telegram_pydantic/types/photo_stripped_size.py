from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoStrippedSize(BaseModel):
    """
    types.PhotoStrippedSize
    ID: 0xe0b0bc2e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoStrippedSize'] = pydantic.Field(
        'types.PhotoStrippedSize',
        alias='_'
    )

    type: str
    bytes: bytes
