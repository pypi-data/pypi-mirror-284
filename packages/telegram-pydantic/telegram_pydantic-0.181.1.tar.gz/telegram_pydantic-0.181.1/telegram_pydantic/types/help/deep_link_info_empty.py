from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeepLinkInfoEmpty(BaseModel):
    """
    types.help.DeepLinkInfoEmpty
    ID: 0x66afa166
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.DeepLinkInfoEmpty'] = pydantic.Field(
        'types.help.DeepLinkInfoEmpty',
        alias='_'
    )

