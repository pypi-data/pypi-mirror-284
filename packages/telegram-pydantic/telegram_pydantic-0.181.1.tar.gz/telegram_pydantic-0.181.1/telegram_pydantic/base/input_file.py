from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputFile - Layer 181
InputFile = typing.Annotated[
    typing.Union[
        types.InputFile,
        types.InputFileBig
    ],
    pydantic.Field(discriminator='QUALNAME')
]
