from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# updates.Difference - Layer 181
Difference = typing.Annotated[
    typing.Union[
        types.updates.Difference,
        types.updates.DifferenceEmpty,
        types.updates.DifferenceSlice,
        types.updates.DifferenceTooLong
    ],
    pydantic.Field(discriminator='QUALNAME')
]
