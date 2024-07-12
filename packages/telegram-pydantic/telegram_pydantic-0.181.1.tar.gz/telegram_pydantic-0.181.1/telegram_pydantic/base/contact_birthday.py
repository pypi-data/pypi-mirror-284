from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ContactBirthday - Layer 181
ContactBirthday = typing.Annotated[
    typing.Union[
        types.ContactBirthday
    ],
    pydantic.Field(discriminator='QUALNAME')
]
