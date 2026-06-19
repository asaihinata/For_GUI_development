"""フォントを設定するモジュール"""

from tkinter import Misc
from tkinter.font import Font
from typing import Literal, overload

from ..readfile import Getfont

__all__ = ["TKFont"]

class TKFont(Font):
    """フォントを設定するオブジェクト"""

    @overload
    def __init__(
        self,
        family: str = "Meiryo",
        size: int | float = 14,
        weight: Literal["normal", "bold"] = "normal",
        slant: Literal["roman", "italic"] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        root: Misc = ...,
    ) -> None:
        """
        :param family: フォント名を指定する
        :type family: str
        :param size: フォントサイズを指定する
        :type size: int | float
        :param weight: フォントの太字を指定する
        :type weight: Literal["normal","bold"]
        :param slant: フォントの斜体を指定する
        :type slant: Literal["roman","italic"]
        :param underline: フォントに下線を付けるか指定する
        :type underline: bool
        :param overstrike: フォントに取り消し線を付けるか指定する
        :type overstrike: bool
        """

    @overload
    def __init__(
        self,
        font: Getfont | Font = ...,
        root: Misc = ...,
    ) -> None: ...
