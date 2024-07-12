from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStrings(BaseModel):
    """
    functions.langpack.GetStrings
    ID: 0xefea3803
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetStrings'] = pydantic.Field(
        'functions.langpack.GetStrings',
        alias='_'
    )

    lang_pack: str
    lang_code: str
    keys: list[str]
