from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Birthday - Layer 181
Birthday = typing.Annotated[
    typing.Union[
        types.Birthday
    ],
    pydantic.Field(discriminator='QUALNAME')
]
