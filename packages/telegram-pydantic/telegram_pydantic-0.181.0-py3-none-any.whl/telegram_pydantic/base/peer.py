from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Peer - Layer 181
Peer = typing.Annotated[
    typing.Union[
        types.PeerChannel,
        types.PeerChat,
        types.PeerUser
    ],
    pydantic.Field(discriminator='QUALNAME')
]
