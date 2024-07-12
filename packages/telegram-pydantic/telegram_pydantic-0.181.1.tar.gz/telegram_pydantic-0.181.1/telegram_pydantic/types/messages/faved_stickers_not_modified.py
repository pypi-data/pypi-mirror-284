from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FavedStickersNotModified(BaseModel):
    """
    types.messages.FavedStickersNotModified
    ID: 0x9e8fa6d3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.FavedStickersNotModified'] = pydantic.Field(
        'types.messages.FavedStickersNotModified',
        alias='_'
    )

