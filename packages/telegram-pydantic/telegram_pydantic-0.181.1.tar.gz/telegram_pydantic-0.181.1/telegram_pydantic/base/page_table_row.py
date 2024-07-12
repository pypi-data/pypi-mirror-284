from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PageTableRow - Layer 181
PageTableRow = typing.Annotated[
    typing.Union[
        types.PageTableRow
    ],
    pydantic.Field(discriminator='QUALNAME')
]
