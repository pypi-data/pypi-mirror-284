from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputFolderPeer(BaseModel):
    """
    types.InputFolderPeer
    ID: 0xfbd2c296
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputFolderPeer'] = pydantic.Field(
        'types.InputFolderPeer',
        alias='_'
    )

    peer: "base.InputPeer"
    folder_id: int
