from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFilterSuggested(BaseModel):
    """
    types.DialogFilterSuggested
    ID: 0x77744d4a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogFilterSuggested'] = pydantic.Field(
        'types.DialogFilterSuggested',
        alias='_'
    )

    filter: "base.DialogFilter"
    description: str
