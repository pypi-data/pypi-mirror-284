from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# EmailVerifyPurpose - Layer 181
EmailVerifyPurpose = typing.Annotated[
    typing.Union[
        types.EmailVerifyPurposeLoginChange,
        types.EmailVerifyPurposeLoginSetup,
        types.EmailVerifyPurposePassport
    ],
    pydantic.Field(discriminator='QUALNAME')
]
