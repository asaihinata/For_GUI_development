from ..btn import *

__all__ = ["Colorbtn"]

class Colorbtn(Btn):
    def get_color(self) -> tuple[tuple[int, int, int], str] | tuple[None, None]:
        """
        選択した色を取得する

        :return: 選択された色のRGBと16進数カラーコードをタプルで((R,G,B),16進数カラーコード)で返す
        :rtype: tuple[tuple[int,int,int],str]|tuple[None,None]
        """

    @property
    def color(self) -> tuple[tuple[int, int, int], str] | tuple[None, None]:
        """
        選択した色を取得する

        :return: 選択された色のRGBと16進数カラーコードをタプルで((R,G,B),16進数カラーコード)で返す
        :rtype: tuple[tuple[int,int,int],str]|tuple[None,None]
        """
