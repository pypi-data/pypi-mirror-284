from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoSizeEmpty(BaseModel):
    """
    types.PhotoSizeEmpty
    ID: 0xe17e23c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoSizeEmpty'] = pydantic.Field(
        'types.PhotoSizeEmpty',
        alias='_'
    )

    type: str
