from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# FolderPeer - Layer 181
FolderPeer = typing.Annotated[
    typing.Union[
        types.FolderPeer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
