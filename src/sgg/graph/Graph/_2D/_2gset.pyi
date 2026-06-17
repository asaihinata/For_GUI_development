from matplotlib.axes._axes import Axes

from ...typing import *

__all__ = ["_2Gset"]

class _2Gset:
    ax: Axes
    def winsize(self) -> TupleInt2:
        """ウィジェットの現在の幅と高さを返す

        :return: ウィジェットの現在の幅と高さをタプルで返す
        :rtype: TupleInt2"""

    def winwidth(self) -> int:
        """ウィジェットの現在の幅を返す

        :return: ウィジェットの現在の幅を返す
        :rtype: int"""

    def winheight(self) -> int:
        """ウィジェットの現在の高さを返す

        :return: ウィジェットの現在の高さを返す
        :rtype: int"""

    def winxy(self) -> TupleInt2:
        """親ウィジェット内での座標を返す

        :return: 親ウィジェット内での座標を返す
        :rtype: TupleInt2"""

    def winx(self) -> int:
        """親ウィジェット内での左端のx座標を返す

        :return: 親ウィジェット内での左端のx座標を返す
        :rtype: int"""

    def winy(self) -> int:
        """親ウィジェット内での上端のy座標を返す

        :return: 親ウィジェット内での上端のy座標を返す
        :rtype: int"""

    def geometry(self) -> TupleFloat4:
        """ウィジェットのサイズと位置を返す

        :return: ウィジェットのサイズと位置を返す
        :rtype: TupleFloat4"""

    def rootxy(self) -> TupleInt2:
        """画面全体に対するウィジェットの座標を返す

        :return: 画面全体に対するウィジェットの座標を返す
        :rtype: TupleInt2"""

    def rootx(self) -> int:
        """画面全体に対するウィジェットの左端のx座標を返す

        :return: 画面全体に対するウィジェットの左端のx座標を返す
        :rtype: int"""

    def rooty(self) -> int:
        """画面全体に対するウィジェットの上端のy座標を返す

        :return: 画面全体に対するウィジェットの上端のy座標を返す
        :rtype: int"""

    def reqsize(self) -> TupleInt2:
        """ウィジェットが必要とする幅の長さと高さを返す

        :return: ウィジェットが必要とする幅の長さと高さを返す
        :rtype: TupleInt2"""

    def reqwidth(self) -> int:
        """ウィジェットが必要とする幅の長さを返す

        :return: ウィジェットが必要とする幅の長さを返す
        :rtype: int"""

    def reqheight(self) -> int:
        """ウィジェットが必要とする高さを返す

        :return: ウィジェットが必要とする高さを返す
        :rtype: int"""

    def visual(self) -> str:
        """色の表現形式を返す"""

    def screen(self) -> str:
        """スクリーンの名前を返す"""

    def id(self) -> int:
        """ウィジェットのウィンドウ識別子を返す"""

    def name(self) -> None:
        """ウィジェットのインスタンス名を返す"""

    def invert(self) -> None:
        """x軸,y軸の軸を反転させる"""

    def invert_x(self) -> None:
        """x軸の軸を反転させる"""

    def invert_y(self) -> None:
        """y軸の軸を反転させる"""

    def getbound(self) -> tuple[Typetuple_float64, Typetuple_float64]:
        """表示されているx軸,y軸の範囲の下限値と上限値を昇順で返す

        :return: x軸,y軸の順で表示されている範囲の下限値と上限値のtupleを返す
        :rtype: tuple[Typetuple_float64,Typetuple_float64]"""

    def getxbound(self) -> Typetuple_float64:
        """表示されているx軸の範囲の下限値と上限値を昇順で返す

        :return: 表示されているx軸の範囲の下限値と上限値のtupleを返す
        :rtype: Typetuple_float64"""

    def getybound(self) -> Typetuple_float64:
        """表示されているy軸の範囲の下限値と上限値を昇順で返す

        :return: 表示されているy軸の範囲の下限値と上限値のtupleを返す
        :rtype: Typetuple_float64"""

    def getticks(self) -> tuple[ndarray, ndarray]:
        """x軸,y軸の目盛りの位置を返す

        :return: x軸,y軸の目盛りの位置を返す
        :rtype: tuple[ndarray,ndarray]"""

    def getxticks(self) -> ndarray:
        """x軸の目盛りの位置を座標で返す

        :return: x軸の目盛りの位置を返す
        :rtype: ndarray"""

    def getyticks(self) -> ndarray:
        """y軸の目盛りの位置を座標で返す

        :return: y軸の目盛りの位置を返す
        :rtype: ndarray"""
