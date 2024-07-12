from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterChatPhotos(BaseModel):
    """
    types.InputMessagesFilterChatPhotos
    ID: 0x3a20ecb8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterChatPhotos'] = pydantic.Field(
        'types.InputMessagesFilterChatPhotos',
        alias='_'
    )

