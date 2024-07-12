from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupCallStreamChannels(BaseModel):
    """
    functions.phone.GetGroupCallStreamChannels
    ID: 0x1ab21940
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupCallStreamChannels'] = pydantic.Field(
        'functions.phone.GetGroupCallStreamChannels',
        alias='_'
    )

    call: "base.InputGroupCall"
