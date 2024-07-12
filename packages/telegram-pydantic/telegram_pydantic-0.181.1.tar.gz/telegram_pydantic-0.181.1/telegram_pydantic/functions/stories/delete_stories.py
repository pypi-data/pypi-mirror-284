from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteStories(BaseModel):
    """
    functions.stories.DeleteStories
    ID: 0xae59db5f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.DeleteStories'] = pydantic.Field(
        'functions.stories.DeleteStories',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
