from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.ValidatedRequestedInfo - Layer 181
ValidatedRequestedInfo = typing.Annotated[
    typing.Union[
        types.payments.ValidatedRequestedInfo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
