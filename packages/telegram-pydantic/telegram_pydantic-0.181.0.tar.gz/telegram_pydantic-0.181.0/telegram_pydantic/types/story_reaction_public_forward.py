from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryReactionPublicForward(BaseModel):
    """
    types.StoryReactionPublicForward
    ID: 0xbbab2643
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryReactionPublicForward'] = pydantic.Field(
        'types.StoryReactionPublicForward',
        alias='_'
    )

    message: "base.Message"
