from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.PeerSettings - Layer 181
PeerSettings = typing.Annotated[
    typing.Union[
        types.messages.PeerSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
