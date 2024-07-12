from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputQuickReplyShortcut - Layer 181
InputQuickReplyShortcut = typing.Annotated[
    typing.Union[
        types.InputQuickReplyShortcut,
        types.InputQuickReplyShortcutId
    ],
    pydantic.Field(discriminator='QUALNAME')
]
