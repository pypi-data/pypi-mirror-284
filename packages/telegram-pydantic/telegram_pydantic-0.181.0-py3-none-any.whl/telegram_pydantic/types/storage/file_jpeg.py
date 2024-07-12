from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileJpeg(BaseModel):
    """
    types.storage.FileJpeg
    ID: 0x7efe0e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileJpeg'] = pydantic.Field(
        'types.storage.FileJpeg',
        alias='_'
    )

