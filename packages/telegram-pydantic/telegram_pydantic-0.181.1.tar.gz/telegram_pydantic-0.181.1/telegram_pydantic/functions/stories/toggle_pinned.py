from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TogglePinned(BaseModel):
    """
    functions.stories.TogglePinned
    ID: 0x9a75a1ef
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.TogglePinned'] = pydantic.Field(
        'functions.stories.TogglePinned',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
    pinned: bool
