from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionWebViewDataSent(BaseModel):
    """
    types.MessageActionWebViewDataSent
    ID: 0xb4c38cb5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionWebViewDataSent'] = pydantic.Field(
        'types.MessageActionWebViewDataSent',
        alias='_'
    )

    text: str
