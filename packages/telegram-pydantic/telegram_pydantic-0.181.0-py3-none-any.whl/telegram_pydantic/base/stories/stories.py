from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# stories.Stories - Layer 181
Stories = typing.Annotated[
    typing.Union[
        types.stories.Stories
    ],
    pydantic.Field(discriminator='QUALNAME')
]
