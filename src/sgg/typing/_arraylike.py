from collections.abc import Sequence
from typing import Any, SupportsIndex

__all__ = [
    "_AnyShape",
    "_Shape",
    "_ShapeLike",
    "Typeaxis",
]
# 形状
type _Shape = tuple[int, ...]
type _AnyShape = tuple[Any, ...]
type _ShapeLike = SupportsIndex | Sequence[SupportsIndex]
# その他
type Typeaxis = _ShapeLike | None
