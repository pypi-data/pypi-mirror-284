from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateAutoSaveSettings(BaseModel):
    """
    types.UpdateAutoSaveSettings
    ID: 0xec05b097
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateAutoSaveSettings'] = pydantic.Field(
        'types.UpdateAutoSaveSettings',
        alias='_'
    )

