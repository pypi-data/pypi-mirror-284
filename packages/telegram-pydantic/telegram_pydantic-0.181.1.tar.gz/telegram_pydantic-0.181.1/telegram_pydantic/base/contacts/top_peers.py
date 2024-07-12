from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# contacts.TopPeers - Layer 181
TopPeers = typing.Annotated[
    typing.Union[
        types.contacts.TopPeers,
        types.contacts.TopPeersDisabled,
        types.contacts.TopPeersNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
