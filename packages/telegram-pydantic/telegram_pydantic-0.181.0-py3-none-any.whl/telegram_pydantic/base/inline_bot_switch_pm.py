from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InlineBotSwitchPM - Layer 181
InlineBotSwitchPM = typing.Annotated[
    typing.Union[
        types.InlineBotSwitchPM
    ],
    pydantic.Field(discriminator='QUALNAME')
]
