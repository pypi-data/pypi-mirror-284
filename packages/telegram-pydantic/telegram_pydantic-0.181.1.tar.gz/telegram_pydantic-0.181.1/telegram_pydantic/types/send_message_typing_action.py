from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageTypingAction(BaseModel):
    """
    types.SendMessageTypingAction
    ID: 0x16bf744e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageTypingAction'] = pydantic.Field(
        'types.SendMessageTypingAction',
        alias='_'
    )

