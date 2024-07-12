from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveAppLog(BaseModel):
    """
    functions.help.SaveAppLog
    ID: 0x6f02f748
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.SaveAppLog'] = pydantic.Field(
        'functions.help.SaveAppLog',
        alias='_'
    )

    events: list["base.InputAppEvent"]
