from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PhoneCall - Layer 181
PhoneCall = typing.Annotated[
    typing.Union[
        types.PhoneCall,
        types.PhoneCallAccepted,
        types.PhoneCallDiscarded,
        types.PhoneCallEmpty,
        types.PhoneCallRequested,
        types.PhoneCallWaiting
    ],
    pydantic.Field(discriminator='QUALNAME')
]
