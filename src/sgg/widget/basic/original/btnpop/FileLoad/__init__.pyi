from ..btn import *

__all__ = ["FileLoad"]

class FileLoad(Btn):
    def __fspath__(self) -> str | None:
        """
        選択したファイルのパスを取得する

        :return: 選択したファイルのパスを返す
        :rtype: str|None
        """

    @property
    def path(self) -> str | None:
        """
        選択したファイルのパスを取得する

        :return: 選択したファイルのパスを返す
        :rtype: str|None
        """

    def get_path(self) -> str | None:
        """
        選択したファイルのパスを取得する

        :return: 選択したファイルのパスを返す
        :rtype: str
        """
