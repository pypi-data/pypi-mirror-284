from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Reactions(BaseModel):
    """
    types.messages.Reactions
    ID: 0xeafdf716
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.Reactions'] = pydantic.Field(
        'types.messages.Reactions',
        alias='_'
    )

    hash: int
    reactions: list["base.Reaction"]
