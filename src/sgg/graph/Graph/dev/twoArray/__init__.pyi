"""グラフ用の配列作成モジュール"""

from typing import Any, Generator

from numpy.typing import ArrayLike, DTypeLike, NDArray

__all__ = ["TwoArray"]

class TwoArray:
    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        xdtype: DTypeLike = object,
        ydtype: DTypeLike = object,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> Generator[NDArray[Any], Any, Any, None]: ...
    @property
    def x(self) -> NDArray: ...
    @property
    def y(self) -> NDArray: ...
    @property
    def data(self) -> NDArray: ...
