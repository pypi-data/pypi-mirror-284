from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SendAsPeer - Layer 181
SendAsPeer = typing.Annotated[
    typing.Union[
        types.SendAsPeer
    ],
    pydantic.Field(discriminator='QUALNAME')
]
