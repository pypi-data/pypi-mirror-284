from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.SavedRingtones - Layer 181
SavedRingtones = typing.Annotated[
    typing.Union[
        types.account.SavedRingtones,
        types.account.SavedRingtonesNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
