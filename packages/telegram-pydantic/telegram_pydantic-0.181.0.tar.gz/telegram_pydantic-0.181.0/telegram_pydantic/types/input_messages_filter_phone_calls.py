from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterPhoneCalls(BaseModel):
    """
    types.InputMessagesFilterPhoneCalls
    ID: 0x80c99768
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterPhoneCalls'] = pydantic.Field(
        'types.InputMessagesFilterPhoneCalls',
        alias='_'
    )

    missed: typing.Optional[bool] = None
