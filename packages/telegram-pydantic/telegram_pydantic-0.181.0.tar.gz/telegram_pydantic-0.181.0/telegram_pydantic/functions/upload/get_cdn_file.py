from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetCdnFile(BaseModel):
    """
    functions.upload.GetCdnFile
    ID: 0x395f69da
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetCdnFile'] = pydantic.Field(
        'functions.upload.GetCdnFile',
        alias='_'
    )

    file_token: bytes
    offset: int
    limit: int
