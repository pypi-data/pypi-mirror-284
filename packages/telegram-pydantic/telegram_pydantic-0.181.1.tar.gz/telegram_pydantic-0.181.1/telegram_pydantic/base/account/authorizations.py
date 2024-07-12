from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.Authorizations - Layer 181
Authorizations = typing.Annotated[
    typing.Union[
        types.account.Authorizations
    ],
    pydantic.Field(discriminator='QUALNAME')
]
