from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColorsNotModified(BaseModel):
    """
    types.help.PeerColorsNotModified
    ID: 0x2ba1f5ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColorsNotModified'] = pydantic.Field(
        'types.help.PeerColorsNotModified',
        alias='_'
    )

