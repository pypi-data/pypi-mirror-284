from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class IncrementStoryViews(BaseModel):
    """
    functions.stories.IncrementStoryViews
    ID: 0xb2028afb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.IncrementStoryViews'] = pydantic.Field(
        'functions.stories.IncrementStoryViews',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
