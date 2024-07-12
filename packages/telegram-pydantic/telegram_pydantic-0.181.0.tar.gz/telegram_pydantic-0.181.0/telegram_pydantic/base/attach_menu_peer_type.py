from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AttachMenuPeerType - Layer 181
AttachMenuPeerType = typing.Annotated[
    typing.Union[
        types.AttachMenuPeerTypeBotPM,
        types.AttachMenuPeerTypeBroadcast,
        types.AttachMenuPeerTypeChat,
        types.AttachMenuPeerTypePM,
        types.AttachMenuPeerTypeSameBotPM
    ],
    pydantic.Field(discriminator='QUALNAME')
]
