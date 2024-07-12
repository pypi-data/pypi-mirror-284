from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionCount(BaseModel):
    """
    types.ReactionCount
    ID: 0xa3d1cb80
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionCount'] = pydantic.Field(
        'types.ReactionCount',
        alias='_'
    )

    reaction: "base.Reaction"
    count: int
    chosen_order: typing.Optional[int] = None
