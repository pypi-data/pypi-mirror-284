from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveRingtone(BaseModel):
    """
    functions.account.SaveRingtone
    ID: 0x3dea5b03
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveRingtone'] = pydantic.Field(
        'functions.account.SaveRingtone',
        alias='_'
    )

    id: "base.InputDocument"
    unsave: bool
