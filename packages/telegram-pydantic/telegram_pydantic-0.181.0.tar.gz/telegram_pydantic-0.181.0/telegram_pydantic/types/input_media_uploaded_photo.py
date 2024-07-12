from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaUploadedPhoto(BaseModel):
    """
    types.InputMediaUploadedPhoto
    ID: 0x1e287d04
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaUploadedPhoto'] = pydantic.Field(
        'types.InputMediaUploadedPhoto',
        alias='_'
    )

    file: "base.InputFile"
    spoiler: typing.Optional[bool] = None
    stickers: typing.Optional[list["base.InputDocument"]] = None
    ttl_seconds: typing.Optional[int] = None
