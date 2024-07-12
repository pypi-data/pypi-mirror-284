from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStory(BaseModel):
    """
    types.UpdateStory
    ID: 0x75b3b798
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStory'] = pydantic.Field(
        'types.UpdateStory',
        alias='_'
    )

    peer: "base.Peer"
    story: "base.StoryItem"
