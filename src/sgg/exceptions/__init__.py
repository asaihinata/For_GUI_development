"""フレームワークで使用する例外のモジュール"""

from typing import Any

import numpy._typing as npt

__all__ = [
    "DtypeError",
    "NoScalarError",
    "ShapeError",
    "UIntError",
]


class DtypeError(ValueError, IndexError):
    """np.ndarrayのdtypeが不正の場合の例外"""

    __dtype: npt.DTypeLike

    def __init__(self, dtype: npt.DTypeLike) -> None:
        self.__dtype = dtype

    def __str__(self) -> str:
        return f'"{self.__dtype}"が不正の型です'


class UIntError(ValueError, IndexError):
    """値が正の整数ではなかった場合のさせる例外"""

    __value: str

    def __init__(self, value: Any) -> None:
        self.__value = value

    def __str__(self) -> str:
        return f"値({self.__value})が正の整数ではありません"


class ShapeError(ValueError, IndexError):
    """配列の形状が不正の場合に発生させる例外"""

    __shape: Any

    def __init__(self, shape: Any) -> None:
        self.__shape = shape

    def __str__(self) -> str:
        return str(f"shape({self.__shape})が正しい値ではありません")


class NoScalarError(ValueError, IndexError):
    """値がスカラー値ではない場合に発生させる例外"""

    __element: Any

    def __init__(self, element: Any) -> None:
        self.__element = element

    def __str__(self) -> str:
        return str(f"{self.__element}はスカラー値ではありません")
