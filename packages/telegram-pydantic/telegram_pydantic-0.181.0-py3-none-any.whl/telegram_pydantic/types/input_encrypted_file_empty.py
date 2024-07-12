from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputEncryptedFileEmpty(BaseModel):
    """
    types.InputEncryptedFileEmpty
    ID: 0x1837c364
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputEncryptedFileEmpty'] = pydantic.Field(
        'types.InputEncryptedFileEmpty',
        alias='_'
    )

