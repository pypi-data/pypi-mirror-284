from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleTopPeers(BaseModel):
    """
    functions.contacts.ToggleTopPeers
    ID: 0x8514bdda
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ToggleTopPeers'] = pydantic.Field(
        'functions.contacts.ToggleTopPeers',
        alias='_'
    )

    enabled: bool
