r"""src\sgg\nparray内の例外メッセージのモジュール"""

__all__ = ["NoScalarError","ShapeError","UIntError",]

class UIntError(ValueError, IndexError):
    """値が正の整数ではなかった場合のさせる例外"""

class ShapeError(ValueError, IndexError):
    """配列の形状が不正の場合に発生させる例外"""

class NoScalarError(ValueError, IndexError):
    """値がスカラー値ではない場合に発生させる例外"""
