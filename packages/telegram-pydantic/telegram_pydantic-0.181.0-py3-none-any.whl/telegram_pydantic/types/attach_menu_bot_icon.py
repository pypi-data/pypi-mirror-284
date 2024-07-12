from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuBotIcon(BaseModel):
    """
    types.AttachMenuBotIcon
    ID: 0xb2a7386b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuBotIcon'] = pydantic.Field(
        'types.AttachMenuBotIcon',
        alias='_'
    )

    name: str
    icon: "base.Document"
    colors: typing.Optional[list["base.AttachMenuBotIconColor"]] = None
