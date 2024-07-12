from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.SupportName - Layer 181
SupportName = typing.Annotated[
    typing.Union[
        types.help.SupportName
    ],
    pydantic.Field(discriminator='QUALNAME')
]
