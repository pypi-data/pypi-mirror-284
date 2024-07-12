from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAttachMenuBots(BaseModel):
    """
    functions.messages.GetAttachMenuBots
    ID: 0x16fcc2cb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAttachMenuBots'] = pydantic.Field(
        'functions.messages.GetAttachMenuBots',
        alias='_'
    )

    hash: int
