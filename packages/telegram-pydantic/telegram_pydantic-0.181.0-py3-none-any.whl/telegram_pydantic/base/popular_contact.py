from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PopularContact - Layer 181
PopularContact = typing.Annotated[
    typing.Union[
        types.PopularContact
    ],
    pydantic.Field(discriminator='QUALNAME')
]
