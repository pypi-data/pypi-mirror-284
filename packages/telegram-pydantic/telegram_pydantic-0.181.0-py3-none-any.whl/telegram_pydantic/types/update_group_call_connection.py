from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateGroupCallConnection(BaseModel):
    """
    types.UpdateGroupCallConnection
    ID: 0xb783982
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateGroupCallConnection'] = pydantic.Field(
        'types.UpdateGroupCallConnection',
        alias='_'
    )

    params: "base.DataJSON"
    presentation: typing.Optional[bool] = None
