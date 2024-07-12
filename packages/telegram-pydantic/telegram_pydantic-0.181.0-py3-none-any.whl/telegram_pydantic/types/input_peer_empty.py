from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerEmpty(BaseModel):
    """
    types.InputPeerEmpty
    ID: 0x7f3b18ea
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerEmpty'] = pydantic.Field(
        'types.InputPeerEmpty',
        alias='_'
    )

