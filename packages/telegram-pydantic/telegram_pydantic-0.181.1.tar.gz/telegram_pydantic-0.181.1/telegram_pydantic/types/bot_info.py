from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotInfo(BaseModel):
    """
    types.BotInfo
    ID: 0x8f300b57
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotInfo'] = pydantic.Field(
        'types.BotInfo',
        alias='_'
    )

    user_id: typing.Optional[int] = None
    description: typing.Optional[str] = None
    description_photo: typing.Optional["base.Photo"] = None
    description_document: typing.Optional["base.Document"] = None
    commands: typing.Optional[list["base.BotCommand"]] = None
    menu_button: typing.Optional["base.BotMenuButton"] = None
