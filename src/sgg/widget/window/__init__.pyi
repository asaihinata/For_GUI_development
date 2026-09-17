from tkinter import Tk, Widget
from typing import Any

from _tkinter import TkappType

from sgg.graph import *
from sgg.widget.basic import *

__all__ = ["WindowController"]

class WindowController:
    """ウィンドウを生成する"""

    __firstlineno__: int
    __module__: str
    __dict__: dict[str, Any]
    __doc__: str
    __sizeof__: int
    def get(self, key: str) -> Any:
        """
        ウィジェットの情報を取得する

        :param key: ウィジェットの情報を取得したい,そのウィジェットの指定された`key`を指定する
        :type key: str
        :rtype: Any
        """

    def get_title(self) -> str:
        """ウィジェットのタイトルを取得する"""

    def set_title(self, title: str) -> None:
        """ウィジェットのタイトルを設置する"""

    def get_style(self) -> dict: ...
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

    def numofwidget(self) -> int:
        """ウィンドウに表示されているウィジェットの数を返す"""

    def widgetdict(self) -> dict[str, Any]:
        """
        ウィジェットの`key`とウィジェットの辞書を返す

        :return: ウィジェットのキー名とウィジェットの辞書を返す
        :rtype: dict[str, Any]
        """

    def widgetlist(self) -> list[str]:
        """
        表示されている全てのウィジェットの`key`名の配列を返す

        :return: ウィジェットのキー名とウィジェットの辞書を返す
        :rtype: list[str]
        """

    def widgetall(self) -> list[Any]:
        """表示されている全てのウィジェットの配列を返す"""

    def keys(self) -> list[str]:
        """ウィジェットのオプション名を取得する"""

    def cget(self, key: str) -> Any:
        """ウィジェットのオプションの値を取得する"""

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

    def resizable(self, width: bool, height: bool) -> None:
        """
        ウィンドウのサイズ変更の許可を指定する

        :param width: ウィンドウの幅のサイズを変更できるか指定する
        :type width: bool
        :param height: ウィンドウの高さのサイズを変更できるか指定する
        :type height: bool
        """
    # property
    @property
    def root(self) -> Tk: ...
    @property
    def style_name_dict(self) -> dict: ...
    @property
    def children(self) -> dict[str, Widget]: ...
    @property
    def tk(self) -> TkappType: ...
