from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoryViewPublicForward(BaseModel):
    """
    types.StoryViewPublicForward
    ID: 0x9083670b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoryViewPublicForward'] = pydantic.Field(
        'types.StoryViewPublicForward',
        alias='_'
    )

    message: "base.Message"
    blocked: typing.Optional[bool] = None
    blocked_my_stories_from: typing.Optional[bool] = None
