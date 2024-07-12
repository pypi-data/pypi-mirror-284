from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryItemDeleted(BaseModel):
    """
    types.StoryItemDeleted
    ID: 0x51e6ee4f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryItemDeleted'] = pydantic.Field(
        'types.StoryItemDeleted',
        alias='_'
    )

    id: int
