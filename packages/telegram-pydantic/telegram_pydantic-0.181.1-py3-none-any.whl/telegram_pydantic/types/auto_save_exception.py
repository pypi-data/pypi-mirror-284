from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AutoSaveException(BaseModel):
    """
    types.AutoSaveException
    ID: 0x81602d47
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AutoSaveException'] = pydantic.Field(
        'types.AutoSaveException',
        alias='_'
    )

    peer: "base.Peer"
    settings: "base.AutoSaveSettings"
