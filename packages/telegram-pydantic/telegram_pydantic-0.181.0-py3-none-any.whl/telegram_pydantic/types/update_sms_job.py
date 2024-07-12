from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSmsJob(BaseModel):
    """
    types.UpdateSmsJob
    ID: 0xf16269d4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSmsJob'] = pydantic.Field(
        'types.UpdateSmsJob',
        alias='_'
    )

    job_id: str
