from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessAwayMessage - Layer 181
BusinessAwayMessage = typing.Annotated[
    typing.Union[
        types.BusinessAwayMessage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
