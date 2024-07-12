from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WebPage - Layer 181
WebPage = typing.Annotated[
    typing.Union[
        types.WebPage,
        types.WebPageEmpty,
        types.WebPageNotModified,
        types.WebPagePending
    ],
    pydantic.Field(discriminator='QUALNAME')
]
