from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportedContact(BaseModel):
    """
    types.ImportedContact
    ID: 0xc13e3c50
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ImportedContact'] = pydantic.Field(
        'types.ImportedContact',
        alias='_'
    )

    user_id: int
    client_id: int
