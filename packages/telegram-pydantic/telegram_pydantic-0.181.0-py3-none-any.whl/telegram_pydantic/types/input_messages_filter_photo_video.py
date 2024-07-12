from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPhotoVideo(BaseModel):
    """
    types.InputMessagesFilterPhotoVideo
    ID: 0x56e9f0e4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPhotoVideo'] = pydantic.Field(
        'types.InputMessagesFilterPhotoVideo',
        alias='_'
    )

