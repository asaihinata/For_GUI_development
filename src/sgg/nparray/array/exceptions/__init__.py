r"""
src\sgg\nparray\array内の例外メッセージのモジュール
"""

__all__ = ["ShapeError"]


class ShapeError(ValueError, IndexError):
    def __init__(self, shape):
        self.__shape = shape

    def __str__(self):
        msg = f"shape({self.__shape})が正しい値ではありません"
        return str(msg)
