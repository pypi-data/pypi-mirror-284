from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputDialogPeer - Layer 181
InputDialogPeer = typing.Annotated[
    typing.Union[
        types.InputDialogPeer,
        types.InputDialogPeerFolder
    ],
    pydantic.Field(discriminator='QUALNAME')
]
