from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TimezonesListNotModified(BaseModel):
    """
    types.help.TimezonesListNotModified
    ID: 0x970708cc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.TimezonesListNotModified'] = pydantic.Field(
        'types.help.TimezonesListNotModified',
        alias='_'
    )

