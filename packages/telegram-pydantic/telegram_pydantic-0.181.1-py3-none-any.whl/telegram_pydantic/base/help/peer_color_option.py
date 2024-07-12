from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.PeerColorOption - Layer 181
PeerColorOption = typing.Annotated[
    typing.Union[
        types.help.PeerColorOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
