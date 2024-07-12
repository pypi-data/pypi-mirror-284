from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# PageBlock - Layer 181
PageBlock = typing.Annotated[
    typing.Union[
        types.PageBlockAnchor,
        types.PageBlockAudio,
        types.PageBlockAuthorDate,
        types.PageBlockBlockquote,
        types.PageBlockChannel,
        types.PageBlockCollage,
        types.PageBlockCover,
        types.PageBlockDetails,
        types.PageBlockDivider,
        types.PageBlockEmbed,
        types.PageBlockEmbedPost,
        types.PageBlockFooter,
        types.PageBlockHeader,
        types.PageBlockKicker,
        types.PageBlockList,
        types.PageBlockMap,
        types.PageBlockOrderedList,
        types.PageBlockParagraph,
        types.PageBlockPhoto,
        types.PageBlockPreformatted,
        types.PageBlockPullquote,
        types.PageBlockRelatedArticles,
        types.PageBlockSlideshow,
        types.PageBlockSubheader,
        types.PageBlockSubtitle,
        types.PageBlockTable,
        types.PageBlockTitle,
        types.PageBlockUnsupported,
        types.PageBlockVideo
    ],
    pydantic.Field(discriminator='QUALNAME')
]
