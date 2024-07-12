from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.TermsOfServiceUpdate - Layer 181
TermsOfServiceUpdate = typing.Annotated[
    typing.Union[
        types.help.TermsOfServiceUpdate,
        types.help.TermsOfServiceUpdateEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
