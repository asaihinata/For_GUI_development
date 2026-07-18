from collections.abc import Sequence
from typing import Any, SupportsIndex

from numpy._typing import _SupportsArray
from numpy.dtypes import StringDType
__all__ = [
    "_AnyShape",
    "_Shape",
    "_ShapeLike",
    "_StringDTypeSupportsArray",
    "Typeaxis",
]
# 形状
type _Shape = tuple[int, ...]
type _AnyShape = tuple[Any, ...]
type _ShapeLike = SupportsIndex | Sequence[SupportsIndex]
"""shapeタプルに変換可能なものなら何でも"""
# 文字列
type _StringDTypeSupportsArray = _SupportsArray[StringDType]
"""可変長文字列型(StringDType)のデータを持った配列"""
# その他
type Typeaxis = _ShapeLike | None
"""`axis`専用の型ヒント"""
