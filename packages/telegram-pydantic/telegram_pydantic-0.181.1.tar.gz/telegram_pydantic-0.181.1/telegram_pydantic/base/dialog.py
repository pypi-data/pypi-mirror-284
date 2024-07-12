from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# Dialog - Layer 181
Dialog = typing.Annotated[
    typing.Union[
        types.Dialog,
        types.DialogFolder
    ],
    pydantic.Field(discriminator='QUALNAME')
]
