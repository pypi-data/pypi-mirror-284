from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageChooseContactAction(BaseModel):
    """
    types.SendMessageChooseContactAction
    ID: 0x628cbc6f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageChooseContactAction'] = pydantic.Field(
        'types.SendMessageChooseContactAction',
        alias='_'
    )

