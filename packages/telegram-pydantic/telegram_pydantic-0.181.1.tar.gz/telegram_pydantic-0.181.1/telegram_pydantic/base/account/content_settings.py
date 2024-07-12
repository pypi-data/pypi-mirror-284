from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.ContentSettings - Layer 181
ContentSettings = typing.Annotated[
    typing.Union[
        types.account.ContentSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
