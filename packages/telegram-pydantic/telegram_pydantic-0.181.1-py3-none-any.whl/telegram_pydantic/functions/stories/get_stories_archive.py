from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoriesArchive(BaseModel):
    """
    functions.stories.GetStoriesArchive
    ID: 0xb4352016
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoriesArchive'] = pydantic.Field(
        'functions.stories.GetStoriesArchive',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_id: int
    limit: int
