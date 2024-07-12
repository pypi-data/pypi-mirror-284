from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PageTableCell - Layer 181
PageTableCell = typing.Annotated[
    typing.Union[
        types.PageTableCell
    ],
    pydantic.Field(discriminator='QUALNAME')
]
