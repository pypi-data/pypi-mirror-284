from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputCollectiblePhone(BaseModel):
    """
    types.InputCollectiblePhone
    ID: 0xa2e214a4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputCollectiblePhone'] = pydantic.Field(
        'types.InputCollectiblePhone',
        alias='_'
    )

    phone: str
