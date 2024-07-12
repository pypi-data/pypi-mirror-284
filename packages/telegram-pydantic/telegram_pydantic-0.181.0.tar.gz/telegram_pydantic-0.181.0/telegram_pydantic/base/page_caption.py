from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PageCaption - Layer 181
PageCaption = typing.Annotated[
    typing.Union[
        types.PageCaption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
