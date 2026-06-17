from ..btn import *

__all__ = ["Savebtn"]

class Savebtn(Btn):
    def __fspath__(self) -> str | None:
        """
        選択したファイルもしくはフォルダのパスを取得する

        :return: 選択したファイルもしくはフォルダのパスを返す
        :rtype: str|None
        """

    @property
    def path(self) -> str | None:
        """
        選択したファイルもしくはフォルダのパスを取得する

        :return: 選択したファイルもしくはフォルダのパスを返す
        :rtype: str|None
        """

    def get_path(self) -> str | None:
        """
        選択したファイルもしくはフォルダのパスを取得する

        :return: 選択したファイルもしくはフォルダのパスを返す
        :rtype: str|None
        """
