from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WebViewMessageSent - Layer 181
WebViewMessageSent = typing.Annotated[
    typing.Union[
        types.WebViewMessageSent
    ],
    pydantic.Field(discriminator='QUALNAME')
]
