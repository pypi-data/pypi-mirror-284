from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PeerBlocked - Layer 181
PeerBlocked = typing.Annotated[
    typing.Union[
        types.PeerBlocked
    ],
    pydantic.Field(discriminator='QUALNAME')
]
