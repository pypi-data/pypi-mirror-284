from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Contact - Layer 181
Contact = typing.Annotated[
    typing.Union[
        types.Contact
    ],
    pydantic.Field(discriminator='QUALNAME')
]
