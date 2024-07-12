from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.ExportedAuthorization - Layer 181
ExportedAuthorization = typing.Annotated[
    typing.Union[
        types.auth.ExportedAuthorization
    ],
    pydantic.Field(discriminator='QUALNAME')
]
