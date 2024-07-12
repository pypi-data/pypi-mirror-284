from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputChatlist - Layer 181
InputChatlist = typing.Annotated[
    typing.Union[
        types.InputChatlistDialogFilter
    ],
    pydantic.Field(discriminator='QUALNAME')
]
