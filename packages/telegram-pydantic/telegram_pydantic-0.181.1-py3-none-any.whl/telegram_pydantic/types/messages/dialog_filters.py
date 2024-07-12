from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFilters(BaseModel):
    """
    types.messages.DialogFilters
    ID: 0x2ad93719
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DialogFilters'] = pydantic.Field(
        'types.messages.DialogFilters',
        alias='_'
    )

    filters: list["base.DialogFilter"]
    tags_enabled: typing.Optional[bool] = None
