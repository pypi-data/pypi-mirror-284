from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatReactionsNone(BaseModel):
    """
    types.ChatReactionsNone
    ID: 0xeafc32bc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatReactionsNone'] = pydantic.Field(
        'types.ChatReactionsNone',
        alias='_'
    )

