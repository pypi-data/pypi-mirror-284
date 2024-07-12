from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# AppWebViewResult - Layer 181
AppWebViewResult = typing.Annotated[
    typing.Union[
        types.AppWebViewResultUrl
    ],
    pydantic.Field(discriminator='QUALNAME')
]
