from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureValueHash - Layer 181
SecureValueHash = typing.Annotated[
    typing.Union[
        types.SecureValueHash
    ],
    pydantic.Field(discriminator='QUALNAME')
]
