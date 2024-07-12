from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.PeerColors - Layer 181
PeerColors = typing.Annotated[
    typing.Union[
        types.help.PeerColors,
        types.help.PeerColorsNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
