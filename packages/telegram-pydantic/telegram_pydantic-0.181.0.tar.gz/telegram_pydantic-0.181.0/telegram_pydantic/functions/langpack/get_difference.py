from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDifference(BaseModel):
    """
    functions.langpack.GetDifference
    ID: 0xcd984aa5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetDifference'] = pydantic.Field(
        'functions.langpack.GetDifference',
        alias='_'
    )

    lang_pack: str
    lang_code: str
    from_version: int
