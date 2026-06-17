from tkinter.ttk import Combobox

from ....base import _Element

__all__ = ["TCombobox"]

class TCombobox(_Element):
    widget: Combobox
    def get_text(self) -> str:
        """
        TComboboxウィジェットに記載されている文字を取得する

        :return: TComboboxウィジェットに記載されている文字を返す
        :rtype: str
        """

    def set_text(self, text: str) -> None:
        """
        TComboboxウィジェットの文字を変更する

        :param text: 文字を指定する
        :type text: str
        """

    def clear(self) -> None:
        """TComboboxウィジェットの文字を削除する"""
