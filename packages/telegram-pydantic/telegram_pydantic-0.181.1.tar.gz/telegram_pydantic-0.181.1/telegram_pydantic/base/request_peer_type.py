from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# RequestPeerType - Layer 181
RequestPeerType = typing.Annotated[
    typing.Union[
        types.RequestPeerTypeBroadcast,
        types.RequestPeerTypeChat,
        types.RequestPeerTypeUser
    ],
    pydantic.Field(discriminator='QUALNAME')
]
