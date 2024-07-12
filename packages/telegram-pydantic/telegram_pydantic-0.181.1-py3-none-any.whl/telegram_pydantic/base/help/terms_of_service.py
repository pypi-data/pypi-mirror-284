from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.TermsOfService - Layer 181
TermsOfService = typing.Annotated[
    typing.Union[
        types.help.TermsOfService
    ],
    pydantic.Field(discriminator='QUALNAME')
]
