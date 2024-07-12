from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadRingtone(BaseModel):
    """
    functions.account.UploadRingtone
    ID: 0x831a83a2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UploadRingtone'] = pydantic.Field(
        'functions.account.UploadRingtone',
        alias='_'
    )

    file: "base.InputFile"
    file_name: str
    mime_type: str
