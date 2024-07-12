from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ConnectedBot - Layer 181
ConnectedBot = typing.Annotated[
    typing.Union[
        types.ConnectedBot
    ],
    pydantic.Field(discriminator='QUALNAME')
]
