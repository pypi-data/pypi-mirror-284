from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageRecordVideoAction(BaseModel):
    """
    types.SendMessageRecordVideoAction
    ID: 0xa187d66f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageRecordVideoAction'] = pydantic.Field(
        'types.SendMessageRecordVideoAction',
        alias='_'
    )

