from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputQuickReplyShortcut(BaseModel):
    """
    types.InputQuickReplyShortcut
    ID: 0x24596d41
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputQuickReplyShortcut'] = pydantic.Field(
        'types.InputQuickReplyShortcut',
        alias='_'
    )

    shortcut: str
