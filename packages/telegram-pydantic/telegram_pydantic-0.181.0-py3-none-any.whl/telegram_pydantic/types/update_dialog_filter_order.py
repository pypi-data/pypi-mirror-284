from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogFilterOrder(BaseModel):
    """
    types.UpdateDialogFilterOrder
    ID: 0xa5d72105
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDialogFilterOrder'] = pydantic.Field(
        'types.UpdateDialogFilterOrder',
        alias='_'
    )

    order: list[int]
