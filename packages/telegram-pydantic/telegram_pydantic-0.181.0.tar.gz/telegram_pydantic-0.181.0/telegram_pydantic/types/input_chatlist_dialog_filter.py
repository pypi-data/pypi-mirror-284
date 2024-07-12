from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChatlistDialogFilter(BaseModel):
    """
    types.InputChatlistDialogFilter
    ID: 0xf3e0da33
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChatlistDialogFilter'] = pydantic.Field(
        'types.InputChatlistDialogFilter',
        alias='_'
    )

    filter_id: int
