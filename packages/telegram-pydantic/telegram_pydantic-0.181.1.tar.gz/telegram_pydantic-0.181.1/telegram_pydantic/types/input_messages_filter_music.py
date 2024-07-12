from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterMusic(BaseModel):
    """
    types.InputMessagesFilterMusic
    ID: 0x3751b49e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterMusic'] = pydantic.Field(
        'types.InputMessagesFilterMusic',
        alias='_'
    )

