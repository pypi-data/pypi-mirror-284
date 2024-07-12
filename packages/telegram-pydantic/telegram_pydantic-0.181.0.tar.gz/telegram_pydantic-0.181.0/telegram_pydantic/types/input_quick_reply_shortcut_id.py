from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputQuickReplyShortcutId(BaseModel):
    """
    types.InputQuickReplyShortcutId
    ID: 0x1190cf1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputQuickReplyShortcutId'] = pydantic.Field(
        'types.InputQuickReplyShortcutId',
        alias='_'
    )

    shortcut_id: int
