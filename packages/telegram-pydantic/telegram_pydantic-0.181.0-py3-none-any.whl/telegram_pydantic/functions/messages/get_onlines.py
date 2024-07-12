from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetOnlines(BaseModel):
    """
    functions.messages.GetOnlines
    ID: 0x6e2be050
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetOnlines'] = pydantic.Field(
        'functions.messages.GetOnlines',
        alias='_'
    )

    peer: "base.InputPeer"
