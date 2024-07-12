from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GlobalPrivacySettings(BaseModel):
    """
    types.GlobalPrivacySettings
    ID: 0x734c4ccb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GlobalPrivacySettings'] = pydantic.Field(
        'types.GlobalPrivacySettings',
        alias='_'
    )

    archive_and_mute_new_noncontact_peers: typing.Optional[bool] = None
    keep_archived_unmuted: typing.Optional[bool] = None
    keep_archived_folders: typing.Optional[bool] = None
    hide_read_marks: typing.Optional[bool] = None
    new_noncontact_peers_require_premium: typing.Optional[bool] = None
