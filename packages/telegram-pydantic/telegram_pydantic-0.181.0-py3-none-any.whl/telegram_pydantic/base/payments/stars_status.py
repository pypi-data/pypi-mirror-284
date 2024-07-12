from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.StarsStatus - Layer 181
StarsStatus = typing.Annotated[
    typing.Union[
        types.payments.StarsStatus
    ],
    pydantic.Field(discriminator='QUALNAME')
]
