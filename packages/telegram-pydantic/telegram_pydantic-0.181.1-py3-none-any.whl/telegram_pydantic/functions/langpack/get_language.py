from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLanguage(BaseModel):
    """
    functions.langpack.GetLanguage
    ID: 0x6a596502
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetLanguage'] = pydantic.Field(
        'functions.langpack.GetLanguage',
        alias='_'
    )

    lang_pack: str
    lang_code: str
