from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.SavedRingtone - Layer 181
SavedRingtone = typing.Annotated[
    typing.Union[
        types.account.SavedRingtone,
        types.account.SavedRingtoneConverted
    ],
    pydantic.Field(discriminator='QUALNAME')
]
