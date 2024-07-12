from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# storage.FileType - Layer 181
FileType = typing.Annotated[
    typing.Union[
        types.storage.FileGif,
        types.storage.FileJpeg,
        types.storage.FileMov,
        types.storage.FileMp3,
        types.storage.FileMp4,
        types.storage.FilePartial,
        types.storage.FilePdf,
        types.storage.FilePng,
        types.storage.FileUnknown,
        types.storage.FileWebp
    ],
    pydantic.Field(discriminator='QUALNAME')
]
