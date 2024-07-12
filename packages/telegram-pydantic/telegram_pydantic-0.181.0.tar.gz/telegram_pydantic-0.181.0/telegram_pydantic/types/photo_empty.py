from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhotoEmpty(BaseModel):
    """
    types.PhotoEmpty
    ID: 0x2331b22d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhotoEmpty'] = pydantic.Field(
        'types.PhotoEmpty',
        alias='_'
    )

    id: int
