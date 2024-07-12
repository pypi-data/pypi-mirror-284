from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChatUploadedPhoto(BaseModel):
    """
    types.InputChatUploadedPhoto
    ID: 0xbdcdaec0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChatUploadedPhoto'] = pydantic.Field(
        'types.InputChatUploadedPhoto',
        alias='_'
    )

    file: typing.Optional["base.InputFile"] = None
    video: typing.Optional["base.InputFile"] = None
    video_start_ts: typing.Optional[float] = None
    video_emoji_markup: typing.Optional["base.VideoSize"] = None
