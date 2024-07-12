from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileCdnRedirect(BaseModel):
    """
    types.upload.FileCdnRedirect
    ID: 0xf18cda44
    Layer: 181
    """
    QUALNAME: typing.Literal['types.upload.FileCdnRedirect'] = pydantic.Field(
        'types.upload.FileCdnRedirect',
        alias='_'
    )

    dc_id: int
    file_token: bytes
    encryption_key: bytes
    encryption_iv: bytes
    file_hashes: list["base.FileHash"]
