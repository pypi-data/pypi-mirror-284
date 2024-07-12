from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSuggestedDialogFilters(BaseModel):
    """
    functions.messages.GetSuggestedDialogFilters
    ID: 0xa29cd42c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSuggestedDialogFilters'] = pydantic.Field(
        'functions.messages.GetSuggestedDialogFilters',
        alias='_'
    )

