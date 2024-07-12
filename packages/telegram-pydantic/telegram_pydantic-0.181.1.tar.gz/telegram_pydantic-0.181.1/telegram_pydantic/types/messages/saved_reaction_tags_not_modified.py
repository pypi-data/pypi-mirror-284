from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedReactionTagsNotModified(BaseModel):
    """
    types.messages.SavedReactionTagsNotModified
    ID: 0x889b59ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedReactionTagsNotModified'] = pydantic.Field(
        'types.messages.SavedReactionTagsNotModified',
        alias='_'
    )

