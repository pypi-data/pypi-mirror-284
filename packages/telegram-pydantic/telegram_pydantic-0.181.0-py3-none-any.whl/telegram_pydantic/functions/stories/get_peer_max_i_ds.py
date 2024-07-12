from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerMaxIDs(BaseModel):
    """
    functions.stories.GetPeerMaxIDs
    ID: 0x535983c3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetPeerMaxIDs'] = pydantic.Field(
        'functions.stories.GetPeerMaxIDs',
        alias='_'
    )

    id: list["base.InputPeer"]
