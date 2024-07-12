from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.WebAuthorizations - Layer 181
WebAuthorizations = typing.Annotated[
    typing.Union[
        types.account.WebAuthorizations
    ],
    pydantic.Field(discriminator='QUALNAME')
]
