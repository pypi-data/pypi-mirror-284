from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputWallPaper - Layer 181
InputWallPaper = typing.Annotated[
    typing.Union[
        types.InputWallPaper,
        types.InputWallPaperNoFile,
        types.InputWallPaperSlug
    ],
    pydantic.Field(discriminator='QUALNAME')
]
