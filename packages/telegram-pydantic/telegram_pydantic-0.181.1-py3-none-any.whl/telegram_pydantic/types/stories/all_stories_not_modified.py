from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllStoriesNotModified(BaseModel):
    """
    types.stories.AllStoriesNotModified
    ID: 0x1158fe3e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stories.AllStoriesNotModified'] = pydantic.Field(
        'types.stories.AllStoriesNotModified',
        alias='_'
    )

    state: str
    stealth_mode: "base.StoriesStealthMode"
