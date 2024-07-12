from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinGroupCall(BaseModel):
    """
    functions.phone.JoinGroupCall
    ID: 0xb132ff7b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.JoinGroupCall'] = pydantic.Field(
        'functions.phone.JoinGroupCall',
        alias='_'
    )

    call: "base.InputGroupCall"
    join_as: "base.InputPeer"
    params: "base.DataJSON"
    muted: typing.Optional[bool] = None
    video_stopped: typing.Optional[bool] = None
    invite_hash: typing.Optional[str] = None
