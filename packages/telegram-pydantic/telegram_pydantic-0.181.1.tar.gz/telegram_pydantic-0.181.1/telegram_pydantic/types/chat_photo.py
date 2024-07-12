from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatPhoto(BaseModel):
    """
    types.ChatPhoto
    ID: 0x1c6e1c11
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatPhoto'] = pydantic.Field(
        'types.ChatPhoto',
        alias='_'
    )

    photo_id: int
    dc_id: int
    has_video: typing.Optional[bool] = None
    stripped_thumb: typing.Optional[bytes] = None
