from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.PeerColorSet - Layer 181
PeerColorSet = typing.Annotated[
    typing.Union[
        types.help.PeerColorProfileSet,
        types.help.PeerColorSet
    ],
    pydantic.Field(discriminator='QUALNAME')
]
