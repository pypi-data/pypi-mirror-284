from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableReactions(BaseModel):
    """
    types.messages.AvailableReactions
    ID: 0x768e3aad
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AvailableReactions'] = pydantic.Field(
        'types.messages.AvailableReactions',
        alias='_'
    )

    hash: int
    reactions: list["base.AvailableReaction"]
