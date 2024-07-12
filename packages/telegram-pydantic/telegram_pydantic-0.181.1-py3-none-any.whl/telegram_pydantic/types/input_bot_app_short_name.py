from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBotAppShortName(BaseModel):
    """
    types.InputBotAppShortName
    ID: 0x908c0407
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBotAppShortName'] = pydantic.Field(
        'types.InputBotAppShortName',
        alias='_'
    )

    bot_id: "base.InputUser"
    short_name: str
