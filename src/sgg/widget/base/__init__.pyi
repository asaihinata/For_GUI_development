from tkinter import Misc, _Cursor

from ...font import TKFont
from ...typing import Callable

__all__ = ["_Element", "Element"]

class _Element(Element):
    widget: None
    master: Misc

class Element:
    master: Misc
    graph: bool = False
    cursor: _Cursor
    back_bg: str
    justify: str
    padx: int | float
    pady: int | float
    relief: str
    fg: str
    bg: str
    borderwidth: int | float
    takefocus: bool
    family: str
    font_size: int | float
    weight: str
    slant: str
    underline: bool
    overstrike: bool
    font: TKFont
    anchor: str
    width: int
    height: int
    def _dwh(
        self, val: int | float, other: int | float | None = None
    ) -> int | float | None:
        """ウィジェットの幅もしくは高さを設定するメソッド"""

    def _exec_funcs(
        self, funcs: function | tuple[function, ...] | None = None
    ) -> Callable | None: ...
    def winsize(self) -> tuple[int, int]:
        """
        ウィジェットの現在の幅と高さを返す

        :return: ウィジェットの現在の幅と高さをタプルで返す
        :rtype: tuple[int,int]
        """

    def winwidth(self) -> int:
        """
        ウィジェットの現在の幅を返す

        :return: ウィジェットの現在の幅を返す
        :rtype: int
        """

    def winheight(self) -> int:
        """
        ウィジェットの現在の高さを返す

        :return: ウィジェットの現在の高さを返す
        :rtype: int
        """

    def winxy(self) -> tuple[int, int]:
        """
        親ウィジェット内での座標を返す

        :return: 親ウィジェット内での座標を返す
        :rtype: tuple[int,int]
        """

    def winx(self) -> int:
        """
        親ウィジェット内での左端のx座標を返す

        :return: 親ウィジェット内での左端のx座標を返す
        :rtype: int
        """

    def winy(self) -> int:
        """
        親ウィジェット内での上端のy座標を返す

        :return: 親ウィジェット内での上端のy座標を返す
        :rtype: int
        """

    def geometry(self) -> tuple[float, float, float, float]:
        """
        ウィジェットのサイズと位置を返す

        :return: ウィジェットのサイズと位置を返す
        :rtype: tuple[float,float,float,float]
        """

    def rootxy(self) -> tuple[int, int]:
        """
        画面全体に対するウィジェットの座標を返す

        :return: 画面全体に対するウィジェットの座標を返す
        :rtype: tuple[int,int]
        """

    def rootx(self) -> int:
        """
        画面全体に対するウィジェットの左端のx座標を返す

        :return: 画面全体に対するウィジェットの左端のx座標を返す
        :rtype: int
        """

    def rooty(self) -> int:
        """
        画面全体に対するウィジェットの上端のy座標を返す

        :return: 画面全体に対するウィジェットの上端のy座標を返す
        :rtype: int
        """

    def reqsize(self) -> tuple[int, int]:
        """
        ウィジェットが必要とする幅の長さと高さを返す

        :return: ウィジェットが必要とする幅の長さと高さを返す
        :rtype: tuple[int,int]
        """

    def reqwidth(self) -> int:
        """
        ウィジェットが必要とする幅の長さを返す

        :return: ウィジェットが必要とする幅の長さを返す
        :rtype: int
        """

    def reqheight(self) -> int:
        """
        ウィジェットが必要とする高さを返す

        :return: ウィジェットが必要とする高さを返す
        :rtype: int
        """

    def visual(self) -> str:
        """色の表現形式を返す"""

    def screen(self) -> str:
        """スクリーンの名前を返す"""

    def id(self) -> int:
        """ウィジェットのウィンドウ識別子を返す"""

    def name(self) -> str:
        """ウィジェットのインスタンス名を返す"""
