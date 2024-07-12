from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.ResolvedPeer - Layer 181
ResolvedPeer = typing.Annotated[
    typing.Union[
        types.contacts.ResolvedPeer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
