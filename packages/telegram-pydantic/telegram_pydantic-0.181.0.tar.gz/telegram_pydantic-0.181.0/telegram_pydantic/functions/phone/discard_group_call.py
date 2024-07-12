from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DiscardGroupCall(BaseModel):
    """
    functions.phone.DiscardGroupCall
    ID: 0x7a777135
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.DiscardGroupCall'] = pydantic.Field(
        'functions.phone.DiscardGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
