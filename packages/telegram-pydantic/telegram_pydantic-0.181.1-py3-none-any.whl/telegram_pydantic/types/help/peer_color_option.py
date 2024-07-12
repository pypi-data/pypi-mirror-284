from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColorOption(BaseModel):
    """
    types.help.PeerColorOption
    ID: 0xadec6ebe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColorOption'] = pydantic.Field(
        'types.help.PeerColorOption',
        alias='_'
    )

    color_id: int
    hidden: typing.Optional[bool] = None
    colors: typing.Optional["base.help.PeerColorSet"] = None
    dark_colors: typing.Optional["base.help.PeerColorSet"] = None
    channel_min_level: typing.Optional[int] = None
    group_min_level: typing.Optional[int] = None
