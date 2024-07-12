from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ApplyBoost(BaseModel):
    """
    functions.premium.ApplyBoost
    ID: 0x6b7da746
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.premium.ApplyBoost'] = pydantic.Field(
        'functions.premium.ApplyBoost',
        alias='_'
    )

    peer: "base.InputPeer"
    slots: typing.Optional[list[int]] = None
