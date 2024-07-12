from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.AutoDownloadSettings - Layer 181
AutoDownloadSettings = typing.Annotated[
    typing.Union[
        types.account.AutoDownloadSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
