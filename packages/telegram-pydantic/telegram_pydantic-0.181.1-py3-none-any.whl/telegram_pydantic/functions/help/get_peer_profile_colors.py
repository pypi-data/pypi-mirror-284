from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerProfileColors(BaseModel):
    """
    functions.help.GetPeerProfileColors
    ID: 0xabcfa9fd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetPeerProfileColors'] = pydantic.Field(
        'functions.help.GetPeerProfileColors',
        alias='_'
    )

    hash: int
