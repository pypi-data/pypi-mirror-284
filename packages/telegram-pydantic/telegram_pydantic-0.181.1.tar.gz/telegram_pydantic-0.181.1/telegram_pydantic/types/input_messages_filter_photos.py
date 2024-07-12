from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPhotos(BaseModel):
    """
    types.InputMessagesFilterPhotos
    ID: 0x9609a51c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPhotos'] = pydantic.Field(
        'types.InputMessagesFilterPhotos',
        alias='_'
    )

