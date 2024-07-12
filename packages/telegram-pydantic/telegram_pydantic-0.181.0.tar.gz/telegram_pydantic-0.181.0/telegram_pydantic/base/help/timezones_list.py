from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.TimezonesList - Layer 181
TimezonesList = typing.Annotated[
    typing.Union[
        types.help.TimezonesList,
        types.help.TimezonesListNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
