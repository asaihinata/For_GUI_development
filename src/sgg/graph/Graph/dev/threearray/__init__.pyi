"""グラフ用の配列作成モジュール"""

from typing import Any, Generator

from numpy.typing import ArrayLike, NDArray

__all__ = ["ThreeArray"]

class ThreeArray:
    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        z: ArrayLike,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> Generator[tuple[Any, Any, Any], Any, None]: ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def z(self): ...
    @property
    def data(self) -> list[list[NDArray[Any]] | Any]: ...
