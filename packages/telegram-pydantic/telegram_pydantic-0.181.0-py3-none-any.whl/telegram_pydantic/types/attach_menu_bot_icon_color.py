from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBotIconColor(BaseModel):
    """
    types.AttachMenuBotIconColor
    ID: 0x4576f3f0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBotIconColor'] = pydantic.Field(
        'types.AttachMenuBotIconColor',
        alias='_'
    )

    name: str
    color: int
