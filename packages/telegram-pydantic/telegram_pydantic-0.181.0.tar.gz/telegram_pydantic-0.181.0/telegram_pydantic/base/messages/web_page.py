from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.WebPage - Layer 181
WebPage = typing.Annotated[
    typing.Union[
        types.messages.WebPage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
