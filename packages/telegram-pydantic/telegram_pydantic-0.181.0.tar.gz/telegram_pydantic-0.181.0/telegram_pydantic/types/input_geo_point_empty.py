from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputGeoPointEmpty(BaseModel):
    """
    types.InputGeoPointEmpty
    ID: 0xe4c123d6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputGeoPointEmpty'] = pydantic.Field(
        'types.InputGeoPointEmpty',
        alias='_'
    )

