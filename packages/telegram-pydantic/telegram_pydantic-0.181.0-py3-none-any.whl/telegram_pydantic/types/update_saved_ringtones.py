from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedRingtones(BaseModel):
    """
    types.UpdateSavedRingtones
    ID: 0x74d8be99
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedRingtones'] = pydantic.Field(
        'types.UpdateSavedRingtones',
        alias='_'
    )

