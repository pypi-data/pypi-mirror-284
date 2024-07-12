from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HidePromoData(BaseModel):
    """
    functions.help.HidePromoData
    ID: 0x1e251c95
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.HidePromoData'] = pydantic.Field(
        'functions.help.HidePromoData',
        alias='_'
    )

    peer: "base.InputPeer"
