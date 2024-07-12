from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DhConfigNotModified(BaseModel):
    """
    types.messages.DhConfigNotModified
    ID: 0xc0e24635
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DhConfigNotModified'] = pydantic.Field(
        'types.messages.DhConfigNotModified',
        alias='_'
    )

    random: bytes
