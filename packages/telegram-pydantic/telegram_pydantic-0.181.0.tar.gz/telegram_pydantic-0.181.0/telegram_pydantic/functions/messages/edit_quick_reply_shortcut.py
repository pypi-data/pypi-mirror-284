from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditQuickReplyShortcut(BaseModel):
    """
    functions.messages.EditQuickReplyShortcut
    ID: 0x5c003cef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditQuickReplyShortcut'] = pydantic.Field(
        'functions.messages.EditQuickReplyShortcut',
        alias='_'
    )

    shortcut_id: int
    shortcut: str
