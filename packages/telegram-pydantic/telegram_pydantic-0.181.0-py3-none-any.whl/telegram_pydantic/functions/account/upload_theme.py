from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UploadTheme(BaseModel):
    """
    functions.account.UploadTheme
    ID: 0x1c3db333
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UploadTheme'] = pydantic.Field(
        'functions.account.UploadTheme',
        alias='_'
    )

    file: "base.InputFile"
    file_name: str
    mime_type: str
    thumb: typing.Optional["base.InputFile"] = None
