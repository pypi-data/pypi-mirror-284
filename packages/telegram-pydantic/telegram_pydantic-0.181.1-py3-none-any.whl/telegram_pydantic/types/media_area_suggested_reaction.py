from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MediaAreaSuggestedReaction(BaseModel):
    """
    types.MediaAreaSuggestedReaction
    ID: 0x14455871
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MediaAreaSuggestedReaction'] = pydantic.Field(
        'types.MediaAreaSuggestedReaction',
        alias='_'
    )

    coordinates: "base.MediaAreaCoordinates"
    reaction: "base.Reaction"
    dark: typing.Optional[bool] = None
    flipped: typing.Optional[bool] = None
