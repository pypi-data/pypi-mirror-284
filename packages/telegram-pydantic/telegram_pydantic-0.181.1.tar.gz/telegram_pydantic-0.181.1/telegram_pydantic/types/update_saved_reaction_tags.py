from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedReactionTags(BaseModel):
    """
    types.UpdateSavedReactionTags
    ID: 0x39c67432
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedReactionTags'] = pydantic.Field(
        'types.UpdateSavedReactionTags',
        alias='_'
    )

