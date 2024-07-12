from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# upload.CdnFile - Layer 181
CdnFile = typing.Annotated[
    typing.Union[
        types.upload.CdnFile,
        types.upload.CdnFileReuploadNeeded
    ],
    pydantic.Field(discriminator='QUALNAME')
]
