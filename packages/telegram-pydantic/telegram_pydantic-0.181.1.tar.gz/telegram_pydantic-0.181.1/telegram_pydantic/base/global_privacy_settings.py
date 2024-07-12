from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# GlobalPrivacySettings - Layer 181
GlobalPrivacySettings = typing.Annotated[
    typing.Union[
        types.GlobalPrivacySettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
