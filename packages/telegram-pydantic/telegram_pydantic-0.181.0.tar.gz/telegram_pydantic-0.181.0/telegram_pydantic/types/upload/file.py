from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class File(BaseModel):
    """
    types.upload.File
    ID: 0x96a18d5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.File'] = pydantic.Field(
        'types.upload.File',
        alias='_'
    )

    type: "base.storage.FileType"
    mtime: int
    bytes: bytes
