from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputCollectible - Layer 181
InputCollectible = typing.Annotated[
    typing.Union[
        types.InputCollectiblePhone,
        types.InputCollectibleUsername
    ],
    pydantic.Field(discriminator='QUALNAME')
]
