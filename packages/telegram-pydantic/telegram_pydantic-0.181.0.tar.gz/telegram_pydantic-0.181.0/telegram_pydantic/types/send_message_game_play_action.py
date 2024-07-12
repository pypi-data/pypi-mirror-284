from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageGamePlayAction(BaseModel):
    """
    types.SendMessageGamePlayAction
    ID: 0xdd6a8f48
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageGamePlayAction'] = pydantic.Field(
        'types.SendMessageGamePlayAction',
        alias='_'
    )

