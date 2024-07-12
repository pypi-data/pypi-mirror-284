from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReadStories(BaseModel):
    """
    functions.stories.ReadStories
    ID: 0xa556dac8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.ReadStories'] = pydantic.Field(
        'functions.stories.ReadStories',
        alias='_'
    )

    peer: "base.InputPeer"
    max_id: int
