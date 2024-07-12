from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputInvoiceMessage(BaseModel):
    """
    types.InputInvoiceMessage
    ID: 0xc5b56859
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputInvoiceMessage'] = pydantic.Field(
        'types.InputInvoiceMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
