from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetTopPeerRating(BaseModel):
    """
    functions.contacts.ResetTopPeerRating
    ID: 0x1ae373ac
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ResetTopPeerRating'] = pydantic.Field(
        'functions.contacts.ResetTopPeerRating',
        alias='_'
    )

    category: "base.TopPeerCategory"
    peer: "base.InputPeer"
