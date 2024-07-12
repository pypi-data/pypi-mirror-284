from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.ResetPasswordResult - Layer 181
ResetPasswordResult = typing.Annotated[
    typing.Union[
        types.account.ResetPasswordFailedWait,
        types.account.ResetPasswordOk,
        types.account.ResetPasswordRequestedWait
    ],
    pydantic.Field(discriminator='QUALNAME')
]
