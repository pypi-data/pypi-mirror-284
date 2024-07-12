from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# UrlAuthResult - Layer 181
UrlAuthResult = typing.Annotated[
    typing.Union[
        types.UrlAuthResultAccepted,
        types.UrlAuthResultDefault,
        types.UrlAuthResultRequest
    ],
    pydantic.Field(discriminator='QUALNAME')
]
