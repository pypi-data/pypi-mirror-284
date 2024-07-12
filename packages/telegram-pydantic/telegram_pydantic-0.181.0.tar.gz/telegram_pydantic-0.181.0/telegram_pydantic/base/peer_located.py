from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PeerLocated - Layer 181
PeerLocated = typing.Annotated[
    typing.Union[
        types.PeerLocated,
        types.PeerSelfLocated
    ],
    pydantic.Field(discriminator='QUALNAME')
]
