from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.LoggedOut - Layer 181
LoggedOut = typing.Annotated[
    typing.Union[
        types.auth.LoggedOut
    ],
    pydantic.Field(discriminator='QUALNAME')
]
