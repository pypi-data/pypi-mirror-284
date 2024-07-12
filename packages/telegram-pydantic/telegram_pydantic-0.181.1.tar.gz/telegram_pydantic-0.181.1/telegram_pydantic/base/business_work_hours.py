from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessWorkHours - Layer 181
BusinessWorkHours = typing.Annotated[
    typing.Union[
        types.BusinessWorkHours
    ],
    pydantic.Field(discriminator='QUALNAME')
]
