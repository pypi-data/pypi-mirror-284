from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedReactionTag(BaseModel):
    """
    types.SavedReactionTag
    ID: 0xcb6ff828
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SavedReactionTag'] = pydantic.Field(
        'types.SavedReactionTag',
        alias='_'
    )

    reaction: "base.Reaction"
    count: int
    title: typing.Optional[str] = None
