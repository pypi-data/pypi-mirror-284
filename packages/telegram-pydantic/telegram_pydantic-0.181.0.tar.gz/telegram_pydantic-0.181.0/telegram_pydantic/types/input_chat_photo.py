from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChatPhoto(BaseModel):
    """
    types.InputChatPhoto
    ID: 0x8953ad37
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChatPhoto'] = pydantic.Field(
        'types.InputChatPhoto',
        alias='_'
    )

    id: "base.InputPhoto"
