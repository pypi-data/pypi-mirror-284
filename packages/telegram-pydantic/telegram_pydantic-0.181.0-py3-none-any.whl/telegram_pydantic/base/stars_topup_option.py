from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StarsTopupOption - Layer 181
StarsTopupOption = typing.Annotated[
    typing.Union[
        types.StarsTopupOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
