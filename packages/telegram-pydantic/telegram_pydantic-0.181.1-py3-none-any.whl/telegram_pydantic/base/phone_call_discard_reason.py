from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PhoneCallDiscardReason - Layer 181
PhoneCallDiscardReason = typing.Annotated[
    typing.Union[
        types.PhoneCallDiscardReasonBusy,
        types.PhoneCallDiscardReasonDisconnect,
        types.PhoneCallDiscardReasonHangup,
        types.PhoneCallDiscardReasonMissed
    ],
    pydantic.Field(discriminator='QUALNAME')
]
