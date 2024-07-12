from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatPhotoEmpty(BaseModel):
    """
    types.ChatPhotoEmpty
    ID: 0x37c1011c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatPhotoEmpty'] = pydantic.Field(
        'types.ChatPhotoEmpty',
        alias='_'
    )

