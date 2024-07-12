from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendReaction(BaseModel):
    """
    functions.stories.SendReaction
    ID: 0x7fd736b2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.SendReaction'] = pydantic.Field(
        'functions.stories.SendReaction',
        alias='_'
    )

    peer: "base.InputPeer"
    story_id: int
    reaction: "base.Reaction"
    add_to_recent: typing.Optional[bool] = None
