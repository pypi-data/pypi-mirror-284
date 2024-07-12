from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.AuthorizationForm - Layer 181
AuthorizationForm = typing.Annotated[
    typing.Union[
        types.account.AuthorizationForm
    ],
    pydantic.Field(discriminator='QUALNAME')
]
