from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FinishJob(BaseModel):
    """
    functions.smsjobs.FinishJob
    ID: 0x4f1ebf24
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.smsjobs.FinishJob'] = pydantic.Field(
        'functions.smsjobs.FinishJob',
        alias='_'
    )

    job_id: str
    error: typing.Optional[str] = None
