from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryViews(BaseModel):
    """
    types.stories.StoryViews
    ID: 0xde9eed1d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.StoryViews'] = pydantic.Field(
        'types.stories.StoryViews',
        alias='_'
    )

    views: list["base.StoryViews"]
    users: list["base.User"]
