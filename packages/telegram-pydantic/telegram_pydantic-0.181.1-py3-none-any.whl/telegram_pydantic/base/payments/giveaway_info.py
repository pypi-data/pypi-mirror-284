from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# payments.GiveawayInfo - Layer 181
GiveawayInfo = typing.Annotated[
    typing.Union[
        types.payments.GiveawayInfo,
        types.payments.GiveawayInfoResults
    ],
    pydantic.Field(discriminator='QUALNAME')
]
