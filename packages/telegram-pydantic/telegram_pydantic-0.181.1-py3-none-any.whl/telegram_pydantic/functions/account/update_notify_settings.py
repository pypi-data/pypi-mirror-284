from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNotifySettings(BaseModel):
    """
    functions.account.UpdateNotifySettings
    ID: 0x84be5b93
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateNotifySettings'] = pydantic.Field(
        'functions.account.UpdateNotifySettings',
        alias='_'
    )

    peer: "base.InputNotifyPeer"
    settings: "base.InputPeerNotifySettings"
