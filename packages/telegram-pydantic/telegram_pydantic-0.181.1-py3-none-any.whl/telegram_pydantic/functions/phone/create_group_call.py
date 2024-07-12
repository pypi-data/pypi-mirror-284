from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateGroupCall(BaseModel):
    """
    functions.phone.CreateGroupCall
    ID: 0x48cdc6d8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.CreateGroupCall'] = pydantic.Field(
        'functions.phone.CreateGroupCall',
        alias='_'
    )

    peer: "base.InputPeer"
    random_id: int
    rtmp_stream: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    schedule_date: typing.Optional[int] = None
