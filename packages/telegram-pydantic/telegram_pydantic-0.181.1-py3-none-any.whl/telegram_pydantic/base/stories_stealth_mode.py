from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# StoriesStealthMode - Layer 181
StoriesStealthMode = typing.Annotated[
    typing.Union[
        types.StoriesStealthMode
    ],
    pydantic.Field(discriminator='QUALNAME')
]
