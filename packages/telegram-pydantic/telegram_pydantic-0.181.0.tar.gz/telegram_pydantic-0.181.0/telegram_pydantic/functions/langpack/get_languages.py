from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetLanguages(BaseModel):
    """
    functions.langpack.GetLanguages
    ID: 0x42c6978f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.langpack.GetLanguages'] = pydantic.Field(
        'functions.langpack.GetLanguages',
        alias='_'
    )

    lang_pack: str
