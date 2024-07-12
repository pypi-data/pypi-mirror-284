from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoPathSize(BaseModel):
    """
    types.PhotoPathSize
    ID: 0xd8214d41
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoPathSize'] = pydantic.Field(
        'types.PhotoPathSize',
        alias='_'
    )

    type: str
    bytes: bytes
