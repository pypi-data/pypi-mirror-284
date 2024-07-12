from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionNotificationsFromContacts(BaseModel):
    """
    types.ReactionNotificationsFromContacts
    ID: 0xbac3a61a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionNotificationsFromContacts'] = pydantic.Field(
        'types.ReactionNotificationsFromContacts',
        alias='_'
    )

