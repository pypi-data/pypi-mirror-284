from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBots(BaseModel):
    """
    types.AttachMenuBots
    ID: 0x3c4301c0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBots'] = pydantic.Field(
        'types.AttachMenuBots',
        alias='_'
    )

    hash: int
    bots: list["base.AttachMenuBot"]
    users: list["base.User"]
