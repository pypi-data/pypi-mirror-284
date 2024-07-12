from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# smsjobs.EligibilityToJoin - Layer 181
EligibilityToJoin = typing.Annotated[
    typing.Union[
        types.smsjobs.EligibleToJoin
    ],
    pydantic.Field(discriminator='QUALNAME')
]
