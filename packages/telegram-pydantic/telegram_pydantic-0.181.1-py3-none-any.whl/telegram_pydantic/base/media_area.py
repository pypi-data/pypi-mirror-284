from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MediaArea - Layer 181
MediaArea = typing.Annotated[
    typing.Union[
        types.InputMediaAreaChannelPost,
        types.InputMediaAreaVenue,
        types.MediaAreaChannelPost,
        types.MediaAreaGeoPoint,
        types.MediaAreaSuggestedReaction,
        types.MediaAreaVenue
    ],
    pydantic.Field(discriminator='QUALNAME')
]
