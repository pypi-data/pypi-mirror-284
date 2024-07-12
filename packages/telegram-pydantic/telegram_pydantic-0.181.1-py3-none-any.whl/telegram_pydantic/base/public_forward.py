from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PublicForward - Layer 181
PublicForward = typing.Annotated[
    typing.Union[
        types.PublicForwardMessage,
        types.PublicForwardStory
    ],
    pydantic.Field(discriminator='QUALNAME')
]
