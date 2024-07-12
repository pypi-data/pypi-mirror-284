from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadEncryptedFile(BaseModel):
    """
    functions.messages.UploadEncryptedFile
    ID: 0x5057c497
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UploadEncryptedFile'] = pydantic.Field(
        'functions.messages.UploadEncryptedFile',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
    file: "base.InputEncryptedFile"
