from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ExportedStoryLink - Layer 181
ExportedStoryLink = typing.Annotated[
    typing.Union[
        types.ExportedStoryLink
    ],
    pydantic.Field(discriminator='QUALNAME')
]
