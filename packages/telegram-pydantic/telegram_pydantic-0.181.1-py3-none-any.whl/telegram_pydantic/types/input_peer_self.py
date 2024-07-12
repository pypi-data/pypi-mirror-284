from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerSelf(BaseModel):
    """
    types.InputPeerSelf
    ID: 0x7da07ec9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerSelf'] = pydantic.Field(
        'types.InputPeerSelf',
        alias='_'
    )

