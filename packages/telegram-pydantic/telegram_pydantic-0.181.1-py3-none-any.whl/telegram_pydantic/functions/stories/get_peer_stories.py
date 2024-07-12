from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerStories(BaseModel):
    """
    functions.stories.GetPeerStories
    ID: 0x2c4ada50
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetPeerStories'] = pydantic.Field(
        'functions.stories.GetPeerStories',
        alias='_'
    )

    peer: "base.InputPeer"
