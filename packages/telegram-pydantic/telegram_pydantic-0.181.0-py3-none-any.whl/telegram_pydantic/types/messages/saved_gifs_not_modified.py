from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedGifsNotModified(BaseModel):
    """
    types.messages.SavedGifsNotModified
    ID: 0xe8025ca2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedGifsNotModified'] = pydantic.Field(
        'types.messages.SavedGifsNotModified',
        alias='_'
    )

