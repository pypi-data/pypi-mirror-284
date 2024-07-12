from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputFolderPeer - Layer 181
InputFolderPeer = typing.Annotated[
    typing.Union[
        types.InputFolderPeer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
