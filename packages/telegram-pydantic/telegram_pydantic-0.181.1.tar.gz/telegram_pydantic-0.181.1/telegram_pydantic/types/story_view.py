from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryView(BaseModel):
    """
    types.StoryView
    ID: 0xb0bdeac5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryView'] = pydantic.Field(
        'types.StoryView',
        alias='_'
    )

    user_id: int
    date: int
    blocked: typing.Optional[bool] = None
    blocked_my_stories_from: typing.Optional[bool] = None
    reaction: typing.Optional["base.Reaction"] = None
