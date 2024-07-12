from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCdnFileHashes(BaseModel):
    """
    functions.upload.GetCdnFileHashes
    ID: 0x91dc3f31
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetCdnFileHashes'] = pydantic.Field(
        'functions.upload.GetCdnFileHashes',
        alias='_'
    )

    file_token: bytes
    offset: int
