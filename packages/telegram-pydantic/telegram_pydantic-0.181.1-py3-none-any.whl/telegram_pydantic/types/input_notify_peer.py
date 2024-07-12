from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyPeer(BaseModel):
    """
    types.InputNotifyPeer
    ID: 0xb8bc5b0c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyPeer'] = pydantic.Field(
        'types.InputNotifyPeer',
        alias='_'
    )

    peer: "base.InputPeer"
