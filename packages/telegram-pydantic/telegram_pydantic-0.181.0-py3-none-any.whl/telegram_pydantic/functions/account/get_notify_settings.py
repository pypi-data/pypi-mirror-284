from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetNotifySettings(BaseModel):
    """
    functions.account.GetNotifySettings
    ID: 0x12b3ad31
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetNotifySettings'] = pydantic.Field(
        'functions.account.GetNotifySettings',
        alias='_'
    )

    peer: "base.InputNotifyPeer"
