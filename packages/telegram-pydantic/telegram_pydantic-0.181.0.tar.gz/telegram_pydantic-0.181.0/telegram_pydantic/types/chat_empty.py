from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatEmpty(BaseModel):
    """
    types.ChatEmpty
    ID: 0x29562865
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatEmpty'] = pydantic.Field(
        'types.ChatEmpty',
        alias='_'
    )

    id: int
