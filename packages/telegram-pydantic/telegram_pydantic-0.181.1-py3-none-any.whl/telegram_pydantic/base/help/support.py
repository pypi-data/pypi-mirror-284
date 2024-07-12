from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.Support - Layer 181
Support = typing.Annotated[
    typing.Union[
        types.help.Support
    ],
    pydantic.Field(discriminator='QUALNAME')
]
