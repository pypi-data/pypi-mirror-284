from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PeerColor - Layer 181
PeerColor = typing.Annotated[
    typing.Union[
        types.PeerColor
    ],
    pydantic.Field(discriminator='QUALNAME')
]
