from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveFilePart(BaseModel):
    """
    functions.upload.SaveFilePart
    ID: 0xb304a621
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.SaveFilePart'] = pydantic.Field(
        'functions.upload.SaveFilePart',
        alias='_'
    )

    file_id: int
    file_part: int
    bytes: bytes
