from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebFile(BaseModel):
    """
    types.upload.WebFile
    ID: 0x21e753bc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.WebFile'] = pydantic.Field(
        'types.upload.WebFile',
        alias='_'
    )

    size: int
    mime_type: str
    file_type: "base.storage.FileType"
    mtime: int
    bytes: bytes
