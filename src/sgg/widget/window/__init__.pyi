from tkinter import Tk
from typing import Any

from ...graph import *
from ..basic import *

__all__ = ["WindowController"]

class WindowController:
    """ウィンドウを生成する"""

    __firstlineno__: int
    __module__: str
    __dict__: dict[str, Any]
    __doc__: str
    __sizeof__: int
    root: Tk
    alpha: float
    def __init__(
        self,
        layout: list = ...,
        alpha: int | float = 1,
        fullscreen: bool = False,
        topmost: bool = False,
        title: str = "window",
        load: function | tuple[function, ...] | None = None,
        bg: str = "#64778d",
        scroll: bool = ...,
        scroll_x: bool = ...,
        scroll_y: bool = ...,
        size: tuple[int | float | None, int | float | None] = (None, None),
        maxmine: bool = False,
        location: tuple[int | float, int | float] = (0, 0),
        resizable: tuple[bool, bool] = ...,
        resizableswidth: bool | None = None,
        resizablesheight: bool | None = None,
    ) -> None: ...
    def get(self, key: str) -> Any:
        """
        ウィジェットの情報を取得する

        :param key: ウィジェットの情報を取得したい,そのウィジェットの指定されたkeyを指定する
        :type key: str
        :rtype: Any
        """

    def get_title(self) -> str:
        """ウィジェットのタイトルを取得する"""

    def set_title(self, title: str) -> None:
        """ウィジェットのタイトルを設置する"""

    def close(self) -> None:
        """windowウィジェットを終了させる"""

    def maxwin(self) -> None:
        """ウィンドウを最大化させる"""

    def minwin(self) -> None:
        """ウィンドウを最小化させる"""

    def run(self) -> None:
        """windowのメインループを実行しウィンドウを表示させる"""

    def scroll_to(self, key: str) -> None:
        """
        keyで指定したウィジェットのところに移動する

        :param key: 移動先のウィジェットのkeyを指定する
        :type key: str
        """

    def widgetcount(self) -> int:
        """
        ウィンドウに表示されているウィジェットの数を返す

        :return: ウィンドウに表示されているウィジェットの数を返す
        :rtype: int
        """

    def widgetdict(self) -> dict[str, Any]:
        """
        ウィジェットの"key"とウィジェットの辞書を返す

        :return: ウィジェットのキー名とウィジェットの辞書を返す
        :rtype: dict[str,Any]
        """

    def widgetlist(self) -> list[str]:
        """
        表示されている全てのウィジェットの"key"名の配列を返す

        :return: ウィジェットのキー名とウィジェットの辞書を返す
        :rtype: list[str]
        """

    def widgetall(self) -> list[Any]:
        """
        表示されている全てのウィジェットの配列を返す

        :return: ウィジェットを返す
        :rtype: list[Any]
        """

    def tookphoto(self, file: str = "window", ex: str = ".png") -> None:
        """
        ウィンドウの画面をスクリーンショットをする

        :param file: ファイル名を指定する
        :type file: str
        :param ex: 画像の拡張名を指定する
        :type ex: str
        """

    def foreground(self, bools: bool = True) -> None:
        """ウィンドウを常に最前面にするか指定する"""

    def fullscreen(self, bools: bool = True) -> None:
        """ウィンドウをフルスクリーンにする操作をする"""

    def set_alpha(self, alpha: float = 1.0) -> None:
        """ウィンドウの透明度を指定する"""

    def get_alpha(self) -> None:
        """ウィンドウの透明度を取得する"""

    def deiconify(self) -> None:
        """ウィンドウを再び画面に表示させる"""

    def withdraw(self) -> None:
        """ウィンドウを非表示にする"""

    def geometry(self) -> list[float, float, float, float]:
        """ウィンドウの高さと幅,座標を返す"""
