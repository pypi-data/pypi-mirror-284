from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# phone.PhoneCall - Layer 181
PhoneCall = typing.Annotated[
    typing.Union[
        types.phone.PhoneCall
    ],
    pydantic.Field(discriminator='QUALNAME')
]
