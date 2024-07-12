from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputClientProxy - Layer 181
InputClientProxy = typing.Annotated[
    typing.Union[
        types.InputClientProxy
    ],
    pydantic.Field(discriminator='QUALNAME')
]
