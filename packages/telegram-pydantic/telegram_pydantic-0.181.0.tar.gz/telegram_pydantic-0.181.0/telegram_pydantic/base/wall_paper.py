from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WallPaper - Layer 181
WallPaper = typing.Annotated[
    typing.Union[
        types.WallPaper,
        types.WallPaperNoFile
    ],
    pydantic.Field(discriminator='QUALNAME')
]
