from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionNotificationsFromAll(BaseModel):
    """
    types.ReactionNotificationsFromAll
    ID: 0x4b9e22a0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionNotificationsFromAll'] = pydantic.Field(
        'types.ReactionNotificationsFromAll',
        alias='_'
    )

