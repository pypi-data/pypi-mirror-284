from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogFilter(BaseModel):
    """
    functions.messages.UpdateDialogFilter
    ID: 0x1ad4a04a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UpdateDialogFilter'] = pydantic.Field(
        'functions.messages.UpdateDialogFilter',
        alias='_'
    )

    id: int
    filter: typing.Optional["base.DialogFilter"] = None
