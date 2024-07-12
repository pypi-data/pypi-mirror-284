from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColorProfileSet(BaseModel):
    """
    types.help.PeerColorProfileSet
    ID: 0x767d61eb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColorProfileSet'] = pydantic.Field(
        'types.help.PeerColorProfileSet',
        alias='_'
    )

    palette_colors: list[int]
    bg_colors: list[int]
    story_colors: list[int]
