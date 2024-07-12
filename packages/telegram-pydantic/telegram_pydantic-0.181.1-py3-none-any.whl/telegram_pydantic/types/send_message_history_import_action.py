from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageHistoryImportAction(BaseModel):
    """
    types.SendMessageHistoryImportAction
    ID: 0xdbda9246
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageHistoryImportAction'] = pydantic.Field(
        'types.SendMessageHistoryImportAction',
        alias='_'
    )

    progress: int
