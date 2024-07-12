from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGameShortName(BaseModel):
    """
    types.InputGameShortName
    ID: 0xc331e80a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGameShortName'] = pydantic.Field(
        'types.InputGameShortName',
        alias='_'
    )

    bot_id: "base.InputUser"
    short_name: str
