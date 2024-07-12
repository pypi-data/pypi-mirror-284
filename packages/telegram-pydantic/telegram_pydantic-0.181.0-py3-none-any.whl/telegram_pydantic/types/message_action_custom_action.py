from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionCustomAction(BaseModel):
    """
    types.MessageActionCustomAction
    ID: 0xfae69f56
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionCustomAction'] = pydantic.Field(
        'types.MessageActionCustomAction',
        alias='_'
    )

    message: str
