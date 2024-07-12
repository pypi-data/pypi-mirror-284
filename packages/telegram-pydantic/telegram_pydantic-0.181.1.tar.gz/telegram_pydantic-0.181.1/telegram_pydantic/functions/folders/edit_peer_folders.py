from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditPeerFolders(BaseModel):
    """
    functions.folders.EditPeerFolders
    ID: 0x6847d0ab
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.folders.EditPeerFolders'] = pydantic.Field(
        'functions.folders.EditPeerFolders',
        alias='_'
    )

    folder_peers: list["base.InputFolderPeer"]
