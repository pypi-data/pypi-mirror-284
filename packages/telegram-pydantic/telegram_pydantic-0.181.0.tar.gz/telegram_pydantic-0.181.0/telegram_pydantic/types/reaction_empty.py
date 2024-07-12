from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionEmpty(BaseModel):
    """
    types.ReactionEmpty
    ID: 0x79f5d419
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionEmpty'] = pydantic.Field(
        'types.ReactionEmpty',
        alias='_'
    )

