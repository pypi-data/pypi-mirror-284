from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StartScheduledGroupCall(BaseModel):
    """
    functions.phone.StartScheduledGroupCall
    ID: 0x5680e342
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.StartScheduledGroupCall'] = pydantic.Field(
        'functions.phone.StartScheduledGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
