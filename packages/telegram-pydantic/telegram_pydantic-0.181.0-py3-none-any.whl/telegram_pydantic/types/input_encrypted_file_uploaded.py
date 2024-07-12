from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFileUploaded(BaseModel):
    """
    types.InputEncryptedFileUploaded
    ID: 0x64bd0306
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFileUploaded'] = pydantic.Field(
        'types.InputEncryptedFileUploaded',
        alias='_'
    )

    id: int
    parts: int
    md5_checksum: str
    key_fingerprint: int
