from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSendAs(BaseModel):
    """
    functions.channels.GetSendAs
    ID: 0xdc770ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetSendAs'] = pydantic.Field(
        'functions.channels.GetSendAs',
        alias='_'
    )

    peer: "base.InputPeer"
