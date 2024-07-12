from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWebFile(BaseModel):
    """
    functions.upload.GetWebFile
    ID: 0x24e6818d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.upload.GetWebFile'] = pydantic.Field(
        'functions.upload.GetWebFile',
        alias='_'
    )

    location: "base.InputWebFileLocation"
    offset: int
    limit: int
