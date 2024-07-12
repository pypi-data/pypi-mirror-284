from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessWeeklyOpen - Layer 181
BusinessWeeklyOpen = typing.Annotated[
    typing.Union[
        types.BusinessWeeklyOpen
    ],
    pydantic.Field(discriminator='QUALNAME')
]
