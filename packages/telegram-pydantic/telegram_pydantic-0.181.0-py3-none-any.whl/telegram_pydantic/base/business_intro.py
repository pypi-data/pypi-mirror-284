from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessIntro - Layer 181
BusinessIntro = typing.Annotated[
    typing.Union[
        types.BusinessIntro
    ],
    pydantic.Field(discriminator='QUALNAME')
]
