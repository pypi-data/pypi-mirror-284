from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBoostsToUnblockRestrictions(BaseModel):
    """
    functions.channels.SetBoostsToUnblockRestrictions
    ID: 0xad399cee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SetBoostsToUnblockRestrictions'] = pydantic.Field(
        'functions.channels.SetBoostsToUnblockRestrictions',
        alias='_'
    )

    channel: "base.InputChannel"
    boosts: int
