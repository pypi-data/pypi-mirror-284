from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WebViewResult - Layer 181
WebViewResult = typing.Annotated[
    typing.Union[
        types.WebViewResultUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
