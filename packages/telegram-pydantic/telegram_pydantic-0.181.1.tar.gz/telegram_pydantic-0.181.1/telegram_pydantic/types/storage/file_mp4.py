from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileMp4(BaseModel):
    """
    types.storage.FileMp4
    ID: 0xb3cea0e4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileMp4'] = pydantic.Field(
        'types.storage.FileMp4',
        alias='_'
    )

