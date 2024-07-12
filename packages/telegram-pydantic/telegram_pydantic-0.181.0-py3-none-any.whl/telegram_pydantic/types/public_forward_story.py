from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PublicForwardStory(BaseModel):
    """
    types.PublicForwardStory
    ID: 0xedf3add0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PublicForwardStory'] = pydantic.Field(
        'types.PublicForwardStory',
        alias='_'
    )

    peer: "base.Peer"
    story: "base.StoryItem"
