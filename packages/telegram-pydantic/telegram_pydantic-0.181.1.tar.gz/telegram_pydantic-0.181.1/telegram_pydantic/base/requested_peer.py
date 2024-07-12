from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# RequestedPeer - Layer 181
RequestedPeer = typing.Annotated[
    typing.Union[
        types.RequestedPeerChannel,
        types.RequestedPeerChat,
        types.RequestedPeerUser
    ],
    pydantic.Field(discriminator='QUALNAME')
]
