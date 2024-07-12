from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveBigFilePart(BaseModel):
    """
    functions.upload.SaveBigFilePart
    ID: 0xde7b673d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.SaveBigFilePart'] = pydantic.Field(
        'functions.upload.SaveBigFilePart',
        alias='_'
    )

    file_id: int
    file_part: int
    file_total_parts: int
    bytes: bytes
