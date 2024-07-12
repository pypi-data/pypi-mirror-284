from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetState(BaseModel):
    """
    functions.updates.GetState
    ID: 0xedd4882a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.updates.GetState'] = pydantic.Field(
        'functions.updates.GetState',
        alias='_'
    )

