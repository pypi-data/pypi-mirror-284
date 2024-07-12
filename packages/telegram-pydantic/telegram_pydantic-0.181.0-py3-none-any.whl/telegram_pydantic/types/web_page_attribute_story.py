from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageAttributeStory(BaseModel):
    """
    types.WebPageAttributeStory
    ID: 0x2e94c3e7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageAttributeStory'] = pydantic.Field(
        'types.WebPageAttributeStory',
        alias='_'
    )

    peer: "base.Peer"
    id: int
    story: typing.Optional["base.StoryItem"] = None
