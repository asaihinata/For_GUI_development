from tkinter.ttk import Treeview

from ....base import _Element

__all__ = ["Tree"]

class Tree(_Element):
    widget: Treeview
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def get_iid(self) -> list:
        """
        Treeウィジェットの全てのiidを取得する

        :return: Treeウィジェットの全てのiidを返す
        :rtype: list
        """

    def expand(self, iid: str) -> None:
        """
        指定した`iid`のツリーを開く

        :param iid: 開きたい`iid`を指定する
        :type iid: str
        """

    def collapse(self, iid: str) -> None:
        """
        指定した`iid`のツリーを閉める

        :param iid: ツリーを閉めたい`iid`を指定する
        :type iid: str
        """

    def get_path(self, iid: str) -> str:
        """
        指定した`iid`のサイド見出しを子孫を含め取得し,それらを結合し返す

        :param iid: `iid`を指定する
        :type iid: str
        :return: 指定した`iid`のサイド見出しを子孫を含め取得し,それらを結合し返す
        :rtype: str
        """

    def add_node(self, parent_iid: str, text: str, data_list: list) -> str:
        """
        指定した`iid`の子要素に新しいツリーを追加する

        :param parent_iid: 追加先の`iid`を指定する
        :type parent_iid: str
        :param text: `iid`のサイド見出しを指定する
        :type text: str
        :param data_list: ツリーのコンテンツを指定する
        :type data_list: list
        :return: 追加された`iid`名を返す
        :rtype: str
        """

    def delete_node(self, iid: str) -> None:
        """
        指定した`iid`を削除する

        :param iid: 削除したい`iid`を指定する
        :type iid: str
        """

    def clear_width(self) -> None:
        """Treeウィジェットのセルの幅を均等に戻す"""
