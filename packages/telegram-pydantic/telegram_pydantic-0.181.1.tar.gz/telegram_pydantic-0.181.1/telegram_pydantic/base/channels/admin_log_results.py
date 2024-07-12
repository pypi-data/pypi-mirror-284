from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# channels.AdminLogResults - Layer 181
AdminLogResults = typing.Annotated[
    typing.Union[
        types.channels.AdminLogResults
    ],
    pydantic.Field(discriminator='QUALNAME')
]
