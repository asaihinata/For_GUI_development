r"""
src\sgg内のモジュールで使用する例外メッセージのモジュール
"""

__all__ = ["UIntError", "ShapeError", "NoScalarError"]


class UIntError(ValueError, IndexError):
    """値が正の整数ではなかった場合のさせる例外"""

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return f"値({self.__value})が正の整数ではありません"


class ShapeError(ValueError, IndexError):
    """配列の形状が不正の場合に発生させる例外"""

    def __init__(self, shape):
        self.__shape = shape

    def __str__(self):
        return str(f"shape({self.__shape})が正しい値ではありません")


class NoScalarError(ValueError, IndexError):
    """値がスカラー値ではない場合に発生させる例外"""

    def __init__(self, element):
        self.__element = element

    def __str__(self):
        return str(f"{self.__element}はスカラー値ではありません")
