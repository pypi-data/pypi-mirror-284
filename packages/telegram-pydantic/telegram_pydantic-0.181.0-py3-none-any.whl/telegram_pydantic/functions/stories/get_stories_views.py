from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoriesViews(BaseModel):
    """
    functions.stories.GetStoriesViews
    ID: 0x28e16cc8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoriesViews'] = pydantic.Field(
        'functions.stories.GetStoriesViews',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
