from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DcOption - Layer 181
DcOption = typing.Annotated[
    typing.Union[
        types.DcOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
