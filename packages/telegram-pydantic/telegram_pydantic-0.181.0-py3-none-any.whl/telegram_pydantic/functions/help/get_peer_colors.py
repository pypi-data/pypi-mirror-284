from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerColors(BaseModel):
    """
    functions.help.GetPeerColors
    ID: 0xda80f42f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPeerColors'] = pydantic.Field(
        'functions.help.GetPeerColors',
        alias='_'
    )

    hash: int
