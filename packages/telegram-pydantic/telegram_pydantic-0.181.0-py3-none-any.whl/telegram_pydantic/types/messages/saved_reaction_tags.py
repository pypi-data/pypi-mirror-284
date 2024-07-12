from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedReactionTags(BaseModel):
    """
    types.messages.SavedReactionTags
    ID: 0x3259950a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedReactionTags'] = pydantic.Field(
        'types.messages.SavedReactionTags',
        alias='_'
    )

    tags: list["base.SavedReactionTag"]
    hash: int
