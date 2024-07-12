from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# upload.WebFile - Layer 181
WebFile = typing.Annotated[
    typing.Union[
        types.upload.WebFile
    ],
    pydantic.Field(discriminator='QUALNAME')
]
