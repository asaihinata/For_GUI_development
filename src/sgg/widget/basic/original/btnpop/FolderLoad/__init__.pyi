from ..btn import *

__all__ = ["FolderLoad"]

class FolderLoad(Btn):
    foldersaves: str | None
    def get_path(self) -> str:
        """
        選択したフォルダのパスを取得する

        :return: 選択したフォルダのパスを返す
        :rtype: str
        """
