from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SavedDialog - Layer 181
SavedDialog = typing.Annotated[
    typing.Union[
        types.SavedDialog
    ],
    pydantic.Field(discriminator='QUALNAME')
]
