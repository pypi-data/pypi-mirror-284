from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryItemSkipped(BaseModel):
    """
    types.StoryItemSkipped
    ID: 0xffadc913
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryItemSkipped'] = pydantic.Field(
        'types.StoryItemSkipped',
        alias='_'
    )

    id: int
    date: int
    expire_date: int
    close_friends: typing.Optional[bool] = None
