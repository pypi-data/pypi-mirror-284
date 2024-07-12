from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogPeer(BaseModel):
    """
    types.DialogPeer
    ID: 0xe56dbf05
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogPeer'] = pydantic.Field(
        'types.DialogPeer',
        alias='_'
    )

    peer: "base.Peer"
