from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportLoginToken(BaseModel):
    """
    functions.auth.ExportLoginToken
    ID: 0xb7e085fe
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ExportLoginToken'] = pydantic.Field(
        'functions.auth.ExportLoginToken',
        alias='_'
    )

    api_id: int
    api_hash: str
    except_ids: list[int]
