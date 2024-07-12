from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuPeerTypePM(BaseModel):
    """
    types.AttachMenuPeerTypePM
    ID: 0xf146d31f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuPeerTypePM'] = pydantic.Field(
        'types.AttachMenuPeerTypePM',
        alias='_'
    )

