from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotApp(BaseModel):
    """
    types.messages.BotApp
    ID: 0xeb50adf5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.BotApp'] = pydantic.Field(
        'types.messages.BotApp',
        alias='_'
    )

    app: "base.BotApp"
    inactive: typing.Optional[bool] = None
    request_write_access: typing.Optional[bool] = None
    has_settings: typing.Optional[bool] = None
