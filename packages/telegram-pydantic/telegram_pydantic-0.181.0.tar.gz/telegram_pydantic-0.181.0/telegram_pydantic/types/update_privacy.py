from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePrivacy(BaseModel):
    """
    types.UpdatePrivacy
    ID: 0xee3b272a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePrivacy'] = pydantic.Field(
        'types.UpdatePrivacy',
        alias='_'
    )

    key: "base.PrivacyKey"
    rules: list["base.PrivacyRule"]
