from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStatus(BaseModel):
    """
    functions.smsjobs.GetStatus
    ID: 0x10a698e8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.GetStatus'] = pydantic.Field(
        'functions.smsjobs.GetStatus',
        alias='_'
    )

