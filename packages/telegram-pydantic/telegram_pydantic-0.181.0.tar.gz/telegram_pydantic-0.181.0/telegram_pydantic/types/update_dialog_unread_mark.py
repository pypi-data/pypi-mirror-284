from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogUnreadMark(BaseModel):
    """
    types.UpdateDialogUnreadMark
    ID: 0xe16459c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDialogUnreadMark'] = pydantic.Field(
        'types.UpdateDialogUnreadMark',
        alias='_'
    )

    peer: "base.DialogPeer"
    unread: typing.Optional[bool] = None
