from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TogglePeerStoriesHidden(BaseModel):
    """
    functions.stories.TogglePeerStoriesHidden
    ID: 0xbd0415c4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.TogglePeerStoriesHidden'] = pydantic.Field(
        'functions.stories.TogglePeerStoriesHidden',
        alias='_'
    )

    peer: "base.InputPeer"
    hidden: bool
