from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AutoDownloadSettings - Layer 181
AutoDownloadSettings = typing.Annotated[
    typing.Union[
        types.AutoDownloadSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
