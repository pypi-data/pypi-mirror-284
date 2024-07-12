from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.TmpPassword - Layer 181
TmpPassword = typing.Annotated[
    typing.Union[
        types.account.TmpPassword
    ],
    pydantic.Field(discriminator='QUALNAME')
]
