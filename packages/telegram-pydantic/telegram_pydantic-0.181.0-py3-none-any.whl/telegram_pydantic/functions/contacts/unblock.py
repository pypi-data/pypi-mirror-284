from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Unblock(BaseModel):
    """
    functions.contacts.Unblock
    ID: 0xb550d328
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.Unblock'] = pydantic.Field(
        'functions.contacts.Unblock',
        alias='_'
    )

    id: "base.InputPeer"
    my_stories_from: typing.Optional[bool] = None
