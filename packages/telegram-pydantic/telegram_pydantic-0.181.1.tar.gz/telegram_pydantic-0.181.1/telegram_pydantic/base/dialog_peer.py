from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DialogPeer - Layer 181
DialogPeer = typing.Annotated[
    typing.Union[
        types.DialogPeer,
        types.DialogPeerFolder
    ],
    pydantic.Field(discriminator='QUALNAME')
]
