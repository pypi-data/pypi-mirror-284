from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDeleteQuickReply(BaseModel):
    """
    types.UpdateDeleteQuickReply
    ID: 0x53e6f1ec
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDeleteQuickReply'] = pydantic.Field(
        'types.UpdateDeleteQuickReply',
        alias='_'
    )

    shortcut_id: int
