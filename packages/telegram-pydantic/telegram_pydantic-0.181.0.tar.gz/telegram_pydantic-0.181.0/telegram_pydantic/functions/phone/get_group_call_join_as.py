from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupCallJoinAs(BaseModel):
    """
    functions.phone.GetGroupCallJoinAs
    ID: 0xef7c213a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupCallJoinAs'] = pydantic.Field(
        'functions.phone.GetGroupCallJoinAs',
        alias='_'
    )

    peer: "base.InputPeer"
