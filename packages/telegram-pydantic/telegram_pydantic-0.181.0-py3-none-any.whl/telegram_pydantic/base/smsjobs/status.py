from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# smsjobs.Status - Layer 181
Status = typing.Annotated[
    typing.Union[
        types.smsjobs.Status
    ],
    pydantic.Field(discriminator='QUALNAME')
]
