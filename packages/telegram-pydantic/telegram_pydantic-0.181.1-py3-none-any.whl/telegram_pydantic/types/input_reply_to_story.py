from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReplyToStory(BaseModel):
    """
    types.InputReplyToStory
    ID: 0x5881323a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReplyToStory'] = pydantic.Field(
        'types.InputReplyToStory',
        alias='_'
    )

    peer: "base.InputPeer"
    story_id: int
