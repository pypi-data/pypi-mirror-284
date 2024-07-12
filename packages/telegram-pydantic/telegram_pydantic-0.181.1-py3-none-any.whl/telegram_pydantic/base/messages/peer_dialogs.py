from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.PeerDialogs - Layer 181
PeerDialogs = typing.Annotated[
    typing.Union[
        types.messages.PeerDialogs
    ],
    pydantic.Field(discriminator='QUALNAME')
]
