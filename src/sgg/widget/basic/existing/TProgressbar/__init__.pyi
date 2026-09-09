from tkinter.ttk import Progressbar
from typing import Literal

from sgg.widget.base import _Element

__all__ = ["TProgressbar"]

class TProgressbar(_Element):
    widget: Progressbar
    def start(self, interval: Literal["idle"] | int | None = None) -> None:
        """TProgressbarをプログレスバーのバーを変化させる"""

    def step(self, amount: float | None = None) -> None:
        """プログレスバーを`amount`だけ増加させる"""

    def stop(self) -> None:
        """TProgressbarをプログレスバーのバーの変化を止める"""

    def get(self) -> int | float:
        """
        TProgressbarの値を取得する

        :return: TProgressbarの値を返す
        :rtype: int | float
        """
