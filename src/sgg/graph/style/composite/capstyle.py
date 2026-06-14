"""閉じられていない線の両端点の描画の方法を設定するモジュール"""

from typing import Literal

__all__ = ["Capstyle"]


class Capstyle:
    def __init__(self, cap: Literal["butt", "round", "projecting"]) -> None:
        """
        閉じられていない線の両端点の描画の方法を指定する

        :param cap: 閉じられていない線の両端点の描画の方法を指定する
        :type cap: Literal['butt','round','projecting']
        :raises TypeError: `cap`に`str`型以外の型を指定した場合に発生させる
        """
        if not isinstance(cap, str):
            raise TypeError("capにはstr型を指定してください")
        if cap in ["butt", "round", "projecting"]:
            self.__cap = cap
        else:
            self.__cap = "butt"

    def __str__(self) -> Literal["butt", "round", "projecting"]:
        return self.__cap

    @property
    def cap(self) -> Literal["butt", "round", "projecting"]:
        return self.__cap
