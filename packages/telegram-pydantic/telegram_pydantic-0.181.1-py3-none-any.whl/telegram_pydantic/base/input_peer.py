from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputPeer - Layer 181
InputPeer = typing.Annotated[
    typing.Union[
        types.InputPeerChannel,
        types.InputPeerChannelFromMessage,
        types.InputPeerChat,
        types.InputPeerEmpty,
        types.InputPeerSelf,
        types.InputPeerUser,
        types.InputPeerUserFromMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
