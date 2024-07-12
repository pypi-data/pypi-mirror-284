from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileMov(BaseModel):
    """
    types.storage.FileMov
    ID: 0x4b09ebbc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileMov'] = pydantic.Field(
        'types.storage.FileMov',
        alias='_'
    )

