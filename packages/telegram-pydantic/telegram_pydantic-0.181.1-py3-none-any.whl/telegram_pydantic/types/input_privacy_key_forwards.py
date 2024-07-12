from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyForwards(BaseModel):
    """
    types.InputPrivacyKeyForwards
    ID: 0xa4dd4c08
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyForwards'] = pydantic.Field(
        'types.InputPrivacyKeyForwards',
        alias='_'
    )

