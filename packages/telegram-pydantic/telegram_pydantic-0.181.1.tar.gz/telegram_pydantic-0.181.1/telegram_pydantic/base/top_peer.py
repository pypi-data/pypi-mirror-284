from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# TopPeer - Layer 181
TopPeer = typing.Annotated[
    typing.Union[
        types.TopPeer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
