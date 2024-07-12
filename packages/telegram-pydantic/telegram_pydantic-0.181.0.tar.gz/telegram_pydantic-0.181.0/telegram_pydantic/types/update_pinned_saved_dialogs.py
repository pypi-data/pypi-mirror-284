from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedSavedDialogs(BaseModel):
    """
    types.UpdatePinnedSavedDialogs
    ID: 0x686c85a6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePinnedSavedDialogs'] = pydantic.Field(
        'types.UpdatePinnedSavedDialogs',
        alias='_'
    )

    order: typing.Optional[list["base.DialogPeer"]] = None
