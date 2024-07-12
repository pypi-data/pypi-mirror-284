from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDialogPeer(BaseModel):
    """
    types.InputDialogPeer
    ID: 0xfcaafeb7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDialogPeer'] = pydantic.Field(
        'types.InputDialogPeer',
        alias='_'
    )

    peer: "base.InputPeer"
