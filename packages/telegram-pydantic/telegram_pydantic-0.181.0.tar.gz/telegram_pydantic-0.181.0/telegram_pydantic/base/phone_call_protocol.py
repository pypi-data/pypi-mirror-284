from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PhoneCallProtocol - Layer 181
PhoneCallProtocol = typing.Annotated[
    typing.Union[
        types.PhoneCallProtocol
    ],
    pydantic.Field(discriminator='QUALNAME')
]
