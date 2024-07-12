from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFile(BaseModel):
    """
    functions.upload.GetFile
    ID: 0xbe5335be
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetFile'] = pydantic.Field(
        'functions.upload.GetFile',
        alias='_'
    )

    location: "base.InputFileLocation"
    offset: int
    limit: int
    precise: typing.Optional[bool] = None
    cdn_supported: typing.Optional[bool] = None
