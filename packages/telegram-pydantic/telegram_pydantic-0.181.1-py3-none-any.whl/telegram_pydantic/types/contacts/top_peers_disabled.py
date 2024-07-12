from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeersDisabled(BaseModel):
    """
    types.contacts.TopPeersDisabled
    ID: 0xb52c939d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.TopPeersDisabled'] = pydantic.Field(
        'types.contacts.TopPeersDisabled',
        alias='_'
    )

