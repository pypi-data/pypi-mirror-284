from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatReactionsAll(BaseModel):
    """
    types.ChatReactionsAll
    ID: 0x52928bca
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatReactionsAll'] = pydantic.Field(
        'types.ChatReactionsAll',
        alias='_'
    )

    allow_custom: typing.Optional[bool] = None
