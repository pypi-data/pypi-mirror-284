from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEditData(BaseModel):
    """
    types.messages.MessageEditData
    ID: 0x26b5dde6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MessageEditData'] = pydantic.Field(
        'types.messages.MessageEditData',
        alias='_'
    )

    caption: typing.Optional[bool] = None
