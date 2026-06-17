from ..btn import *

__all__ = ["FolderLoad"]

class FolderLoad(Btn):
    def __fspath__(self) -> str | None:
        """
        選択したフォルダのパスを取得する

        :return: 選択したフォルダのパスを返す
        :rtype: str|None
        """

    @property
    def path(self) -> str | None:
        """
        選択したフォルダのパスを取得する

        :return: 選択したフォルダのパスを返す
        :rtype: str|None
        """

    def get_path(self) -> str | None:
        """
        選択したフォルダのパスを取得する

        :return: 選択したフォルダのパスを返す
        :rtype: str|None
        """
