from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSettings(BaseModel):
    """
    functions.smsjobs.UpdateSettings
    ID: 0x93fa0bf
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.UpdateSettings'] = pydantic.Field(
        'functions.smsjobs.UpdateSettings',
        alias='_'
    )

    allow_international: typing.Optional[bool] = None
