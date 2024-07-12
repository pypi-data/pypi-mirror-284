from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleAllStoriesHidden(BaseModel):
    """
    functions.stories.ToggleAllStoriesHidden
    ID: 0x7c2557c4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.ToggleAllStoriesHidden'] = pydantic.Field(
        'functions.stories.ToggleAllStoriesHidden',
        alias='_'
    )

    hidden: bool
