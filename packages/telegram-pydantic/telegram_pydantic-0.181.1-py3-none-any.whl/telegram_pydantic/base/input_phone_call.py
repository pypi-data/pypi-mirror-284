from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputPhoneCall - Layer 181
InputPhoneCall = typing.Annotated[
    typing.Union[
        types.InputPhoneCall
    ],
    pydantic.Field(discriminator='QUALNAME')
]
