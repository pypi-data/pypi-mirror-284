from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveDefaultGroupCallJoinAs(BaseModel):
    """
    functions.phone.SaveDefaultGroupCallJoinAs
    ID: 0x575e1f8c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SaveDefaultGroupCallJoinAs'] = pydantic.Field(
        'functions.phone.SaveDefaultGroupCallJoinAs',
        alias='_'
    )

    peer: "base.InputPeer"
    join_as: "base.InputPeer"
