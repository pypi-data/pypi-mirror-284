from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileHash(BaseModel):
    """
    types.FileHash
    ID: 0xf39b035c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.FileHash'] = pydantic.Field(
        'types.FileHash',
        alias='_'
    )

    offset: int
    limit: int
    hash: bytes
