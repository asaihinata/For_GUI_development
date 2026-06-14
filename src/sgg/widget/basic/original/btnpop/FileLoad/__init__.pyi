from ..btn import *

__all__ = ["FileLoad"]

class FileLoad(Btn):
    filesaves: str | None
    def get_path(self) -> str:
        """
        選択したファイルのパスを取得する

        :return: 選択したファイルのパスを返す
        :rtype: str
        """
