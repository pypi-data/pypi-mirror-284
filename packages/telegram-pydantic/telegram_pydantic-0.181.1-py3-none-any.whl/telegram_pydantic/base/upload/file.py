from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# upload.File - Layer 181
File = typing.Annotated[
    typing.Union[
        types.upload.File,
        types.upload.FileCdnRedirect
    ],
    pydantic.Field(discriminator='QUALNAME')
]
