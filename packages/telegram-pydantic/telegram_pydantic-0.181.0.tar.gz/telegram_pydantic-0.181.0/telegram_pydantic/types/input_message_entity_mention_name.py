from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessageEntityMentionName(BaseModel):
    """
    types.InputMessageEntityMentionName
    ID: 0x208e68c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessageEntityMentionName'] = pydantic.Field(
        'types.InputMessageEntityMentionName',
        alias='_'
    )

    offset: int
    length: int
    user_id: "base.InputUser"
