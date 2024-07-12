from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SimpleWebViewResult - Layer 181
SimpleWebViewResult = typing.Annotated[
    typing.Union[
        types.SimpleWebViewResultUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
