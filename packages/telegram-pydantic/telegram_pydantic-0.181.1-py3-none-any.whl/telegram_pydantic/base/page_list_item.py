from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PageListItem - Layer 181
PageListItem = typing.Annotated[
    typing.Union[
        types.PageListItemBlocks,
        types.PageListItemText
    ],
    pydantic.Field(discriminator='QUALNAME')
]
