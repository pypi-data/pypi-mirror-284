from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.EmailVerified - Layer 181
EmailVerified = typing.Annotated[
    typing.Union[
        types.account.EmailVerified,
        types.account.EmailVerifiedLogin
    ],
    pydantic.Field(discriminator='QUALNAME')
]
