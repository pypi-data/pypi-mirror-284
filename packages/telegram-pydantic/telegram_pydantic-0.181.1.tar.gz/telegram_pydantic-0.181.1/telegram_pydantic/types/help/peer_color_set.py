from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColorSet(BaseModel):
    """
    types.help.PeerColorSet
    ID: 0x26219a58
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColorSet'] = pydantic.Field(
        'types.help.PeerColorSet',
        alias='_'
    )

    colors: list[int]
