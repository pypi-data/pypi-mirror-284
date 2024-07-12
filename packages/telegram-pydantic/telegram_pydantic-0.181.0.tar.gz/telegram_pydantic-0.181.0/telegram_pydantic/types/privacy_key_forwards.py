from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyForwards(BaseModel):
    """
    types.PrivacyKeyForwards
    ID: 0x69ec56a3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyForwards'] = pydantic.Field(
        'types.PrivacyKeyForwards',
        alias='_'
    )

