from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmailVerification - Layer 181
EmailVerification = typing.Annotated[
    typing.Union[
        types.EmailVerificationApple,
        types.EmailVerificationCode,
        types.EmailVerificationGoogle
    ],
    pydantic.Field(discriminator='QUALNAME')
]
