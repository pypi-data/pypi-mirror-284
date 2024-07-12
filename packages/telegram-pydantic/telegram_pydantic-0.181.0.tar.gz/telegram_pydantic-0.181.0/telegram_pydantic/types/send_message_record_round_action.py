from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageRecordRoundAction(BaseModel):
    """
    types.SendMessageRecordRoundAction
    ID: 0x88f27fbc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageRecordRoundAction'] = pydantic.Field(
        'types.SendMessageRecordRoundAction',
        alias='_'
    )

