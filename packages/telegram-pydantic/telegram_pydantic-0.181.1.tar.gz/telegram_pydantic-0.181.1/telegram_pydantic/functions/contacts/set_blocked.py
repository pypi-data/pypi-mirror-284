from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBlocked(BaseModel):
    """
    functions.contacts.SetBlocked
    ID: 0x94c65c76
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.SetBlocked'] = pydantic.Field(
        'functions.contacts.SetBlocked',
        alias='_'
    )

    id: list["base.InputPeer"]
    limit: int
    my_stories_from: typing.Optional[bool] = None
