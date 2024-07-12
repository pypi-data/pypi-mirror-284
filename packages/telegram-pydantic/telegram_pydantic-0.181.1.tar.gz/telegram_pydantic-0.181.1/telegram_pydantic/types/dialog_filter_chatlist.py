from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFilterChatlist(BaseModel):
    """
    types.DialogFilterChatlist
    ID: 0x9fe28ea4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogFilterChatlist'] = pydantic.Field(
        'types.DialogFilterChatlist',
        alias='_'
    )

    id: int
    title: str
    pinned_peers: list["base.InputPeer"]
    include_peers: list["base.InputPeer"]
    has_my_invites: typing.Optional[bool] = None
    emoticon: typing.Optional[str] = None
    color: typing.Optional[int] = None
