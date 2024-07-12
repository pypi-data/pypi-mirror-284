from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFileHashes(BaseModel):
    """
    functions.upload.GetFileHashes
    ID: 0x9156982a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetFileHashes'] = pydantic.Field(
        'functions.upload.GetFileHashes',
        alias='_'
    )

    location: "base.InputFileLocation"
    offset: int
