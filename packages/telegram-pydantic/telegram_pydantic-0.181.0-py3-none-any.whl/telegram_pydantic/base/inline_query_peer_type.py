from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InlineQueryPeerType - Layer 181
InlineQueryPeerType = typing.Annotated[
    typing.Union[
        types.InlineQueryPeerTypeBotPM,
        types.InlineQueryPeerTypeBroadcast,
        types.InlineQueryPeerTypeChat,
        types.InlineQueryPeerTypeMegagroup,
        types.InlineQueryPeerTypePM,
        types.InlineQueryPeerTypeSameBotPM
    ],
    pydantic.Field(discriminator='QUALNAME')
]
