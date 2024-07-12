from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StickersNotModified(BaseModel):
    """
    types.messages.StickersNotModified
    ID: 0xf1749a22
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.StickersNotModified'] = pydantic.Field(
        'types.messages.StickersNotModified',
        alias='_'
    )

