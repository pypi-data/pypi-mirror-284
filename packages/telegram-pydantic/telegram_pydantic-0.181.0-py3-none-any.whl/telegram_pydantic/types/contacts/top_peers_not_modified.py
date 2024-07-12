from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeersNotModified(BaseModel):
    """
    types.contacts.TopPeersNotModified
    ID: 0xde266ef5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.TopPeersNotModified'] = pydantic.Field(
        'types.contacts.TopPeersNotModified',
        alias='_'
    )

