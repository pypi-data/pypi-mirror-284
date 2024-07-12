from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDocumentEmpty(BaseModel):
    """
    types.InputDocumentEmpty
    ID: 0x72f0eaae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDocumentEmpty'] = pydantic.Field(
        'types.InputDocumentEmpty',
        alias='_'
    )

