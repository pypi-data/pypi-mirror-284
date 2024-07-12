from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AttachMenuBot - Layer 181
AttachMenuBot = typing.Annotated[
    typing.Union[
        types.AttachMenuBot
    ],
    pydantic.Field(discriminator='QUALNAME')
]
