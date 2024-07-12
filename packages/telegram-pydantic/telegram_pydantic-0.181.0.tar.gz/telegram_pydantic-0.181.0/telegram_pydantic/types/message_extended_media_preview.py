from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageExtendedMediaPreview(BaseModel):
    """
    types.MessageExtendedMediaPreview
    ID: 0xad628cc8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageExtendedMediaPreview'] = pydantic.Field(
        'types.MessageExtendedMediaPreview',
        alias='_'
    )

    w: typing.Optional[int] = None
    h: typing.Optional[int] = None
    thumb: typing.Optional["base.PhotoSize"] = None
    video_duration: typing.Optional[int] = None
