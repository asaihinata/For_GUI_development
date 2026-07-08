r"""
src\sgg内のモジュールで使用する例外メッセージのモジュール
"""

__all__=["UIntError"]

class UIntError(ValueError, IndexError):
    """値が正の整数ではなかった場合の例外"""

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return str(f"値({self.__value})が正の整数ではありません")
