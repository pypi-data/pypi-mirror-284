from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBotsNotModified(BaseModel):
    """
    types.AttachMenuBotsNotModified
    ID: 0xf1d88a5c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBotsNotModified'] = pydantic.Field(
        'types.AttachMenuBotsNotModified',
        alias='_'
    )

