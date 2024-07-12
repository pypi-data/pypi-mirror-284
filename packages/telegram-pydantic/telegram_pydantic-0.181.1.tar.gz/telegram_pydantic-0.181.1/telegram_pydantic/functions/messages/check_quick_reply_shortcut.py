from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckQuickReplyShortcut(BaseModel):
    """
    functions.messages.CheckQuickReplyShortcut
    ID: 0xf1d0fbd3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CheckQuickReplyShortcut'] = pydantic.Field(
        'functions.messages.CheckQuickReplyShortcut',
        alias='_'
    )

    shortcut: str
