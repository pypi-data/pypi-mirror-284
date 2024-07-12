from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MediaAreaCoordinates - Layer 181
MediaAreaCoordinates = typing.Annotated[
    typing.Union[
        types.MediaAreaCoordinates
    ],
    pydantic.Field(discriminator='QUALNAME')
]
