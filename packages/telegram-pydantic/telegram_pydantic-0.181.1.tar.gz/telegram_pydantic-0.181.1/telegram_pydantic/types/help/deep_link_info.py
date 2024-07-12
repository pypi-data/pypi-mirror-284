from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeepLinkInfo(BaseModel):
    """
    types.help.DeepLinkInfo
    ID: 0x6a4ee832
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.DeepLinkInfo'] = pydantic.Field(
        'types.help.DeepLinkInfo',
        alias='_'
    )

    message: str
    update_app: typing.Optional[bool] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
