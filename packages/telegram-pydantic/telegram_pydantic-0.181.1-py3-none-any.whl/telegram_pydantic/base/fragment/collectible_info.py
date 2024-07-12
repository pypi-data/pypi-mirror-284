from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# fragment.CollectibleInfo - Layer 181
CollectibleInfo = typing.Annotated[
    typing.Union[
        types.fragment.CollectibleInfo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
