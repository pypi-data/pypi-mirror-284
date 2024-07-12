from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatReactionsSome(BaseModel):
    """
    types.ChatReactionsSome
    ID: 0x661d4037
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatReactionsSome'] = pydantic.Field(
        'types.ChatReactionsSome',
        alias='_'
    )

    reactions: list["base.Reaction"]
