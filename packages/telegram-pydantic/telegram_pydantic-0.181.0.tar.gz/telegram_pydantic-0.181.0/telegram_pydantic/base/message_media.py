from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageMedia - Layer 181
MessageMedia = typing.Annotated[
    typing.Union[
        types.MessageMediaContact,
        types.MessageMediaDice,
        types.MessageMediaDocument,
        types.MessageMediaEmpty,
        types.MessageMediaGame,
        types.MessageMediaGeo,
        types.MessageMediaGeoLive,
        types.MessageMediaGiveaway,
        types.MessageMediaGiveawayResults,
        types.MessageMediaInvoice,
        types.MessageMediaPhoto,
        types.MessageMediaPoll,
        types.MessageMediaStory,
        types.MessageMediaUnsupported,
        types.MessageMediaVenue,
        types.MessageMediaWebPage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
