from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStoryID(BaseModel):
    """
    types.UpdateStoryID
    ID: 0x1bf335b9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateStoryID'] = pydantic.Field(
        'types.UpdateStoryID',
        alias='_'
    )

    id: int
    random_id: int
