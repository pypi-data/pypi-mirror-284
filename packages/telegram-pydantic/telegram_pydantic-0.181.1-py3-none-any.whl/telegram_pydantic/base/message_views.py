from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessageViews - Layer 181
MessageViews = typing.Annotated[
    typing.Union[
        types.MessageViews
    ],
    pydantic.Field(discriminator='QUALNAME')
]
