from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.Authorization - Layer 181
Authorization = typing.Annotated[
    typing.Union[
        types.auth.Authorization,
        types.auth.AuthorizationSignUpRequired
    ],
    pydantic.Field(discriminator='QUALNAME')
]
