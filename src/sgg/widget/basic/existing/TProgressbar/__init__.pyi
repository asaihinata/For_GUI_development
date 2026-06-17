from tkinter.ttk import Progressbar

from ....base import _Element

__all__ = ["TProgressbar"]

class TProgressbar(_Element):
    widget: Progressbar
    def start(self) -> None:
        """TProgressbarをプログレスバーのバーを変化させる"""

    def stop(self) -> None:
        """TProgressbarをプログレスバーのバーの変化を止める"""

    def set(self, val: int | float) -> None:
        """
        TProgressbarウィジェットの値を指定する

        :param val: TProgressbarウィジェットの値を指定する
        :type val: int|float
        """

    def get(self) -> int | float:
        """
        TProgressbarの値を取得する

        :return: TProgressbarの値を返す
        :rtype: int|float
        """
