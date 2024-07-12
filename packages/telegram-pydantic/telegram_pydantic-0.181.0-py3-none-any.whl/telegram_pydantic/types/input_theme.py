from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputTheme(BaseModel):
    """
    types.InputTheme
    ID: 0x3c5693e9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputTheme'] = pydantic.Field(
        'types.InputTheme',
        alias='_'
    )

    id: int
    access_hash: int
