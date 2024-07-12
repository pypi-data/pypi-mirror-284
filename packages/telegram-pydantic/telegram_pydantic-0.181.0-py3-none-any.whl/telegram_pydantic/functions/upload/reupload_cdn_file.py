from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReuploadCdnFile(BaseModel):
    """
    functions.upload.ReuploadCdnFile
    ID: 0x9b2754a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.ReuploadCdnFile'] = pydantic.Field(
        'functions.upload.ReuploadCdnFile',
        alias='_'
    )

    file_token: bytes
    request_token: bytes
