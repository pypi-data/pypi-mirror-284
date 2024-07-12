from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AutoSaveException - Layer 181
AutoSaveException = typing.Annotated[
    typing.Union[
        types.AutoSaveException
    ],
    pydantic.Field(discriminator='QUALNAME')
]
