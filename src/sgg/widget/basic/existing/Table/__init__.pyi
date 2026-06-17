from tkinter.ttk import Treeview

from ....base import _Element

__all__ = ["Table"]

class Table(_Element):
    widget: Treeview
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def clear_width(self) -> None:
        """Tableウィジェットのセルの幅を均等に戻す"""
