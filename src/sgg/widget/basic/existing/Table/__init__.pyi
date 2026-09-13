from tkinter.ttk import Treeview

from sgg.widget.base import TElement

__all__ = ["Table"]

class Table(TElement):
    @property
    def widget(self) -> Treeview: ...
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def clear_width(self) -> None:
        """Tableウィジェットのセルの幅を均等に戻す"""
