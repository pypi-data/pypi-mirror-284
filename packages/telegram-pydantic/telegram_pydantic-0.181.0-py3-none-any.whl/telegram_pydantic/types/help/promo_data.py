from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PromoData(BaseModel):
    """
    types.help.PromoData
    ID: 0x8c39793f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PromoData'] = pydantic.Field(
        'types.help.PromoData',
        alias='_'
    )

    expires: int
    peer: "base.Peer"
    chats: list["base.Chat"]
    users: list["base.User"]
    proxy: typing.Optional[bool] = None
    psa_type: typing.Optional[str] = None
    psa_message: typing.Optional[str] = None
