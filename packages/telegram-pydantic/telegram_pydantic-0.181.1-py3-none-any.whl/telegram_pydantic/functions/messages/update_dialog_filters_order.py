from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogFiltersOrder(BaseModel):
    """
    functions.messages.UpdateDialogFiltersOrder
    ID: 0xc563c1e4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UpdateDialogFiltersOrder'] = pydantic.Field(
        'functions.messages.UpdateDialogFiltersOrder',
        alias='_'
    )

    order: list[int]
