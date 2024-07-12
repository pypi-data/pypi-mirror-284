from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedDialogsNotModified(BaseModel):
    """
    types.messages.SavedDialogsNotModified
    ID: 0xc01f6fe8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedDialogsNotModified'] = pydantic.Field(
        'types.messages.SavedDialogsNotModified',
        alias='_'
    )

    count: int
