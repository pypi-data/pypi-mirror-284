from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TimezonesList(BaseModel):
    """
    types.help.TimezonesList
    ID: 0x7b74ed71
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.TimezonesList'] = pydantic.Field(
        'types.help.TimezonesList',
        alias='_'
    )

    timezones: list["base.Timezone"]
    hash: int
