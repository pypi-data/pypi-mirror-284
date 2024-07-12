from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PageRelatedArticle - Layer 181
PageRelatedArticle = typing.Annotated[
    typing.Union[
        types.PageRelatedArticle
    ],
    pydantic.Field(discriminator='QUALNAME')
]
