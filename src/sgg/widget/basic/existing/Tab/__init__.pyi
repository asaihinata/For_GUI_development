from tkinter import Widget
from tkinter.ttk import Notebook

from sgg.widget.element import TElement

__all__ = ["Tab"]

class Tab(TElement):
    @property
    def widget(self) -> Notebook: ...
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def _add_tab(self, frame: Widget, title: str = ...) -> None:
        """
        Tabウィジェットに新しいタブを追加する

        :param frame: 親ウィジェットを指定する
        :type frame: Widget
        :param title: タイトルを指定する
        :type title: str
        """
