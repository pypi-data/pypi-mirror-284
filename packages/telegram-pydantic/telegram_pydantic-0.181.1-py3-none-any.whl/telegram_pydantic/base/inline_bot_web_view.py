from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InlineBotWebView - Layer 181
InlineBotWebView = typing.Annotated[
    typing.Union[
        types.InlineBotWebView
    ],
    pydantic.Field(discriminator='QUALNAME')
]
