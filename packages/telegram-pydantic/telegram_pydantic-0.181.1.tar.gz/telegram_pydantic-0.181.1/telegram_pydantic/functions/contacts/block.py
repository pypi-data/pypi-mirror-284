from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Block(BaseModel):
    """
    functions.contacts.Block
    ID: 0x2e2e8734
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.Block'] = pydantic.Field(
        'functions.contacts.Block',
        alias='_'
    )

    id: "base.InputPeer"
    my_stories_from: typing.Optional[bool] = None
