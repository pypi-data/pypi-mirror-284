from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StatsGroupTopInviter(BaseModel):
    """
    types.StatsGroupTopInviter
    ID: 0x535f779d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StatsGroupTopInviter'] = pydantic.Field(
        'types.StatsGroupTopInviter',
        alias='_'
    )

    user_id: int
    invitations: int
