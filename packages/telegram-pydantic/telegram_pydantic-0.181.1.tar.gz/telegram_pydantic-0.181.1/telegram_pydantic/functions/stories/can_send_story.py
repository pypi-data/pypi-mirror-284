from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CanSendStory(BaseModel):
    """
    functions.stories.CanSendStory
    ID: 0xc7dfdfdd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.CanSendStory'] = pydantic.Field(
        'functions.stories.CanSendStory',
        alias='_'
    )

    peer: "base.InputPeer"
