from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSmsJob(BaseModel):
    """
    functions.smsjobs.GetSmsJob
    ID: 0x778d902f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.GetSmsJob'] = pydantic.Field(
        'functions.smsjobs.GetSmsJob',
        alias='_'
    )

    job_id: str
