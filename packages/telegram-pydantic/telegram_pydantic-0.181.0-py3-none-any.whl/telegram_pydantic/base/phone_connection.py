from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PhoneConnection - Layer 181
PhoneConnection = typing.Annotated[
    typing.Union[
        types.PhoneConnection,
        types.PhoneConnectionWebrtc
    ],
    pydantic.Field(discriminator='QUALNAME')
]
