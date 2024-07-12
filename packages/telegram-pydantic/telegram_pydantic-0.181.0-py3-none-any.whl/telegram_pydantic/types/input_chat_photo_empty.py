from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChatPhotoEmpty(BaseModel):
    """
    types.InputChatPhotoEmpty
    ID: 0x1ca48f57
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChatPhotoEmpty'] = pydantic.Field(
        'types.InputChatPhotoEmpty',
        alias='_'
    )

