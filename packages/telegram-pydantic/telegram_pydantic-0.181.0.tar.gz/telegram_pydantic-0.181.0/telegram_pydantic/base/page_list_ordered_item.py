from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PageListOrderedItem - Layer 181
PageListOrderedItem = typing.Annotated[
    typing.Union[
        types.PageListOrderedItemBlocks,
        types.PageListOrderedItemText
    ],
    pydantic.Field(discriminator='QUALNAME')
]
