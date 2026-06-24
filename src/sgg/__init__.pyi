from io import BytesIO
from pathlib import Path, PosixPath, WindowsPath
from tkinter import _Cursor

from matplotlib.mlab import GaussianKDE
from numpy.typing import ArrayLike

from .dialogs import *
from .graph import *
from .nparray import *
from .readfile import Getcsv, Getfont, Getjosn
from .typing import *
from .version import __version__
from .widget import *

Type_Marker: TypeAlias = Literal[
    ".",
    ",",
    "o",
    "v",
    "^",
    "<",
    ">",
    "1",
    "2",
    "3",
    "4",
    "8",
    "s",
    "p",
    "*",
    "h",
    "H",
    "+",
    "x",
    "D",
    "d",
    "|",
    "_",
    "P",
    "X",
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    "None",
    "none",
    " ",
    "",
]
Type_Solid: TypeAlias = Literal["-", "--", "-.", ":", "None", " ", ""]
__all__: list[str] = (
    ["__version__", "Getjosn", "Getfont", "Getcsv", "Guis"]
    + getattr(dialogs, "__all__", [])
    + getattr(graph, "__all__", [])
    + getattr(nparray, "__all__", [])
    + getattr(widget, "__all__", [])
)

def __dir__() -> list[str]: ...

class Guis:
    @overload
    @classmethod
    def window(
        cls,
        layout: list = ...,
        alpha: int | float = 1,
        fullscreen: bool = False,
        topmost: bool = False,
        title: str = "window",
        load: function | tuple[function, ...] | None = None,
        bg: str = "#64778d",
        scroll: bool = ...,
        scroll_x: bool = ...,
        scroll_y: bool = ...,
        size: tuple[int | float | None, int | float | None] = (None, None),
        maxmine: bool = False,
        location: tuple[int | float, int | float] = (0, 0),
        resizable: bool | None = ...,
        resizableswidth: bool = ...,
        resizablesheight: bool = ...,
    ) -> WindowController:
        """
        ウィンドウを作成する

        :param layout: ウィンドウで表示されるウィジェットを指定する各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます
        :type layout: Listlike
        :param title: ウィンドウに表示されるタイトル名を指定する
        :type title: str
        :param load: ウィンドウ表示時に実行される関数を指定する
        :type load: function | tuple[function,...] | None
        :param bg: ウィンドウの背景を指定する
        :type bg: ColorTypeN
        :param scroll: ウィンドウのx軸,y軸方向にスクロールできるか指定する
        :type scroll: bool
        :param scroll_x: ウィンドウのx軸方向にスクロールできるか指定する
        :type scroll_x: bool
        :param scroll_y: ウィンドウのy軸方向にスクロールできるか指定する
        :type scroll_y: bool
        :param size: ウィンドウの幅と高さを指定する
        :type size: tuple[int | float | None,int | float | None]
        :param maxmine: ウィンドウ表示時最大化するかを指定する
        :type maxmine: bool
        :param location: ウィンドウの表示位置を指定する
        :type location: tuple[int | float,int | float]
        :param resizable: 幅と高さのサイズ変更の許可を指定する
        :type resizable: bool | None
        :param resizableswidth: 幅のサイズ変更の許可を指定する
        :type resizableswidth: bool
        :param resizablesheight: 高さのサイズ変更の許可を指定する
        :type resizablesheight: bool
        """

    @overload
    @classmethod
    def window(
        cls,
        layout: list = ...,
        alpha: int | float = 1,
        fullscreen: bool = False,
        topmost: bool = False,
        title: str = "window",
        load: function | tuple[function, ...] | None = None,
        bg: str = "#64778d",
        scroll: bool = ...,
        scroll_x: bool = ...,
        scroll_y: bool = ...,
        size: tuple[int | float | None, int | float | None] = (None, None),
        maxmine: bool = False,
        location: tuple[int | float, int | float] = (0, 0),
        resizable: bool = ...,
    ) -> WindowController:
        """
        ウィンドウを作成する

        :param layout: ウィンドウで表示されるウィジェットを指定する各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます
        :type layout: Listlike
        :param title: ウィンドウに表示されるタイトル名を指定する
        :type title: str
        :param load: ウィンドウ表示時に実行される関数を指定する
        :type load: function | tuple[function,...] | None
        :param bg: ウィンドウの背景を指定する
        :type bg: ColorTypeN
        :param scroll: ウィンドウのx軸,y軸方向にスクロールできるか指定する
        :type scroll: bool
        :param scroll_x: ウィンドウのx軸方向にスクロールできるか指定する
        :type scroll_x: bool
        :param scroll_y: ウィンドウのy軸方向にスクロールできるか指定する
        :type scroll_y: bool
        :param size: ウィンドウの幅と高さを指定する
        :type size: tuple[int | float | None,int | float | None]
        :param maxmine: ウィンドウ表示時最大化するかを指定する
        :type maxmine: bool
        :param location: ウィンドウの表示位置を指定する
        :type location: tuple[int | float,int | float]
        :param resizable: 幅と高さのサイズ変更の許可を指定する
        :type resizable: bool
        """

    @overload
    @classmethod
    def window(
        cls,
        layout: list = ...,
        alpha: int | float = 1,
        fullscreen: bool = False,
        topmost: bool = False,
        title: str = "window",
        load: function | tuple[function, ...] | None = None,
        bg: str = "#64778d",
        scroll: bool = ...,
        scroll_x: bool = ...,
        scroll_y: bool = ...,
        size: tuple[int | float | None, int | float | None] = (None, None),
        maxmine: bool = False,
        location: tuple[int | float, int | float] = (0, 0),
        resizable: None = None,
        resizableswidth: bool = ...,
        resizablesheight: bool = ...,
    ) -> WindowController:
        """
        ウィンドウを作成する

        :param layout: ウィンドウで表示されるウィジェットを指定する各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます
        :type layout: Listlike
        :param title: ウィンドウに表示されるタイトル名を指定する
        :type title: str
        :param load: ウィンドウ表示時に実行される関数を指定する
        :type load: function | tuple[function,...] | None
        :param bg: ウィンドウの背景を指定する
        :type bg: ColorTypeN
        :param scroll: ウィンドウのx軸,y軸方向にスクロールできるか指定する
        :type scroll: bool
        :param scroll_x: ウィンドウのx軸方向にスクロールできるか指定する
        :type scroll_x: bool
        :param scroll_y: ウィンドウのy軸方向にスクロールできるか指定する
        :type scroll_y: bool
        :param size: ウィンドウの幅と高さを指定する
        :type size: tuple[int | float | None,int | float | None]
        :param maxmine: ウィンドウ表示時最大化するかを指定する
        :type maxmine: bool
        :param location: ウィンドウの表示位置を指定する
        :type location: tuple[int | float,int | float]
        :param resizable: 幅と高さのサイズ変更の許可を指定する
        :type resizable: None
        :param resizableswidth: 幅のサイズ変更の許可を指定する
        :type resizableswidth: bool
        :param resizablesheight: 高さのサイズ変更の許可を指定する
        :type resizablesheight: bool
        """

    @staticmethod
    def Texts(
        text: str = ...,
        width: int | float | None = ...,
        height: int | float | None = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        takefocus: bool = ...,
        borderwidth: int | float = 0,
        padx: int | float = ...,
        pady: int | float = ...,
        wraplength: int | float = 0,
        cursor: _Cursor = ...,
        justify: Literal["left", "center", "right"] = "left",
        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        テキストを作成する

        :param text: Textsウィジェットに表記させる文字を指定する
        :type text: str
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Link(
        link: str | WindowsPath | PosixPath | Path,
        text: str = ...,
        takefocus: bool = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        wraplength: int | float = 0,
        cursor: _Cursor = ...,
        borderwidth: int | float = 0,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = "#0000ee",
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = True,
        overstrike: bool = ...,
        width: int | float | None = ...,
        height: int | float | None = ...,
        justify: Literal["left", "center", "right"] = "left",
        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        リンクテキストを作成する

        :param link: Linkウィジェットが押されたときにブラウザで開くURLのリンクもしくはhtmlファイルのパスを指定する
        :type link: str | WindowsPath | PosixPath | Path
        :param text: Linkウィジェットに表記させる文字を指定する
        :type text: str
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Images(
        path: WindowsPath | PosixPath | Path = ...,
        takefocus: bool = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        画像を作成する

        :param path: Imagesウィジェットに表示させる画像のパスを指定する
        :type path: WindowsPath | PosixPath | Path
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Imagebyte(
        byte: bytes | BytesIO = ..., takefocus: bool = ..., key: str | None = ...
    ) -> dict[str, Any]:
        """
        画像を作成する

        :param byte: Imagebytoに表示させるバイトデータを指定する
        :type byte: bytes | BytesIO
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Imagelink(
        link: str = ..., takefocus: bool = ..., key: str | None = ...
    ) -> dict[str, Any]:
        """
        画像を作成する

        :param link: 画像リンクを指定する
        :type link: str
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Buttons(
        text: str = ...,
        function: function | tuple[function, ...] | None = ...,
        takefocus: bool = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        wraplength: int | float = 0,
        cursor: _Cursor = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        borderwidth: int | float = 0,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        width: int | float | None = ...,
        height: int | float | None = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        anchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "center",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ボタンを作成する

        :param text: Buttonsウィジェットに表記させる文字を指定する
        :type text: str
        :param function: Buttonsウィジェットが押された時実行される関数を指定する
        :type function: function | tuple[function,...] | None
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Input(
        text: str = ...,
        show: str = ...,
        insertwidth: int | float = 2,
        insertbg: ColorTypeN = "#000000",
        width: int | float = 20,
        borderwidth: int | float = 0,
        takefocus: bool = ...,
        cursor: _Cursor = ...,
        bg: ColorTypeN = "#e0e0e0",
        fg: ColorTypeN = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        justify: Literal["left", "center", "right"] = "left",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        入力欄を作成する

        :param text: Inputウィジェットに表記させる文字を指定する
        :type text: str
        :param insertwidth: Inputウィジェットの入力時の挿入ポイントの幅を指定する
        :type insertwidth: int | float
        :param insertbg: Inputウィジェットの入力時の挿入ポイントの色を指定する
        :type insertbg: ColorTypeN
        :param show: 実際の入力内容の各文字の代わりに表示させる文字を指定する
        :type show: str
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Multiline(
        text: str = ...,
        insertbg: ColorTypeN = "#000000",
        insertwidth: int | float = 2,
        state: Literal["normal", "disabled"] = "normal",
        width: int | float = 20,
        height: int | float = 5,
        wrap: Literal["none", "word", "char"] = "none",
        borderwidth: int | float = 1,
        takefocus: bool = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        justify: Literal["left", "center", "right"] = "left",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        テキストエリアを作成する

        :param text: Multilineウィジェットに表記させる文字を指定する
        :type text: str
        :param insertbg: Multilineウィジェットの入力時の挿入ポイントの色を指定する
        :type insertbg: ColorTypeN
        :param insertwidth: Multilineウィジェットの入力時の挿入ポイントの幅を指定する
        :type insertwidth: int | float
        :param wrap: Multilineウィジェットの折り返しについて指定する
        :type wrap: Literal["none", "word", "char"]
        :param state: 選択操作の有無を指定するnormalは操作可能にするdisabledは操作不可能にする
        :type state: Literal["normal","disabled"]
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Table(
        header_fg: ColorTypeN = "#000000",
        header_bg: ColorTypeN = "#cccccc",
        values: list = ...,
        header: list = ...,
        height: int = 1,
        rowheader: list = ...,
        colwidth: int | float = 120,
        rowheight: int | float = 50,
        bg: ColorTypeN = "#e0e0e0",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        表を作成する

        :param header_fg: Tableウィジェットの見出しの文字色を指定する
        :type header_fg: ColorTypeN
        :param header_bg: Tableウィジェットの見出しの背景色を指定する
        :type header_bg: ColorTypeN
        :param values: Tableウィジェット本体に表示させる文字の配列を指定する
        :type values: list
        :param header: Tableウィジェット見出しに表示させる文字の配列を指定する
        :type header: list
        :param rowheader: Tableウィジェットの縦列の見出しを配列で指定し,それを設置する
        :type rowheader: list
        :param colwidth: Tableウィジェットの幅を指定する
        :type colwidth: int | float
        :param rowheight: Tableウィジェットのセルの高さを指定する
        :type rowheight: int | float
        :param height: Tableウィジェットに表示できる行を指定する
        :type height: int
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Tree(
        values: list = ...,
        header: list = ...,
        bg: ColorTypeN = "#e0e0e0",
        colwidth: int | float = 120,
        header_fg: ColorTypeN = "#000000",
        header_bg: ColorTypeN = "#cccccc",
        rowheight: int | float = 50,
        side_header: str = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ツリーを作成する

        :param header_fg: Treeウィジェットの見出しの文字色を指定する
        :type header_fg: ColorTypeN
        :param header_bg: Treeウィジェットの見出しの背景色を指定する
        :type header_bg: ColorTypeN
        :param side_header: Treeウィジェットの階層列のテキストを指定する
        :type side_header: str
        :param values: Treeウィジェット本体に表示させる文字の配列を指定する
        :type values: list
        :param header: Treeウィジェット見出しに表示させる文字の配列を指定する
        :type header: list
        :param colwidth: Treeウィジェットの幅を指定する
        :type colwidth: int | float
        :param rowheight: Treeウィジェットのセルの高さを指定する
        :type rowheight: int | float
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Listboxs(
        values: list | tuple = ...,
        width: int | float = 20,
        height: int = 5,
        selectfg: ColorTypeN = "#000000",
        selectbg: ColorTypeN = "#1967d2",
        select: int = 0,
        exportselection: bool = False,
        selectmode: Literal["browse", "single", "multiple", "extended"] = "browse",
        state: Literal["normal", "disabled"] = "normal",
        cursor: _Cursor = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#e0e0e0",
        borderwidth: int | float = 0,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        リストボックスを作成する

        :param values: Listboxウィジェットに表記させるリストを指定する
        :type values: list | tuple
        :param selectfg: Listboxウィジェットのリストに選択されているリストの文字色を指定する
        :type selectfg: ColorTypeN
        :param selectbg: Listboxウィジェットのリストに選択されているリストの背景色を指定する
        :type selectbg: ColorTypeN
        :param select: 選択項目の初期値を指定する
        :type select: int
        :param exportselection: 選択中の項目のコピー操作を指定する
        :type exportselection: bool
        :param state: 選択操作の有無を指定するnormalは操作可能にするdisabledは操作不可能にする
        :type state: Literal["normal","disabled"]
        :param selectmode: 選択可能な項目数と操作方法を指定する
        :type selectmode: Literal["browse","single","multiple","extended"]
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def TCombobox(
        values: list = ...,
        default: str = ...,
        state: Literal["normal", "readonly", "disabled"] = "normal",
        takefocus: bool = ...,
        cursor: _Cursor = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        コンボボックスを作成する

        :param values: 選択項目を指定する
        :type values: list
        :param default: 入力項目の初期テキストを指定する
        :type default: str
        :param state: 値の入力制限やTComboboxウィジェットの有効化や無効化について指定する
        :type state: Literal["normal","readonly","disabled"]
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Radio(
        text: str = ...,
        group: str = "default",
        bg: ColorType = ...,
        fg: ColorType = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        takefocus: bool = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        cursor: _Cursor = ...,
        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
        wraplength: int | float = 0,
        borderwidth: int | float = 0,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ラジオボタンを作成する

        読み込み時,グループの最初のRadioウィジェットが選択される
        :param text: Radioウィジェットに表記させる文字を指定する
        :type text: str
        :param group: Radioウィジェットのグループを指定する同じ名前にすることで,そのグループ内で排他的な選択を実施する
        :type group: str
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Checkbox(
        text: str = ...,
        default: bool = False,
        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        wraplength: int | float = 0,
        borderwidth: int | float = 0,
        cursor: _Cursor = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        チェックボタンを作成する

        :param text: Checkboxウィジェットに表記させる文字を指定する
        :type text: str
        :param default: 読み込み時,Checkboxウィジェットがチェックするかを指定する
        :type default: bool
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Frames(
        layout: list = ...,
        title: str = ...,
        labelanchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "nw",
        takefocus: bool = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        relief: Literal[
            "raised", "sunken", "flat", "ridge", "solid", "groove"
        ] = "solid",
        borderwidth: int | float = 1,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        枠線付きのフレームを作成する

        :param layout: Framesウィジェットに表示させるウィジェットを指定する各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます
        :type layout: list[list]
        :param title: Framesウィジェットのタイトルを指定する
        :type title: str
        :param labelanchor: タイトルを表記する場所を指定する
        :type labelanchor: Literal["nw","n","ne","w","center","e","sw","s","se"]
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Menus(
        list: list = ...,
        tearoff: bool = False,
        takefocus: bool = ...,
        cursor: _Cursor = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        borderwidth: int | float = 0,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        メニューバーを作成する

        :param list: Menusウィジェットに表示させるメニューを指定する
        :type list: list
        :param tearoff: メニューウィジェットを独立したウィンドウにするかを指定する
        :type tearoff: bool
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Menubuttons(
        list: list = ...,
        text: str = ...,
        tearoff: bool = False,
        takefocus: bool = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        borderwidth: int | float = 0,
        anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"] = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        メニューボタンを作成する

        :param list: MenuButtonsウィジェットに表示させるメニューを指定する
        :type list: list
        :param text: MenuButtonsウィジェットのボタンに表記させる文字を指定する
        :type text: str
        :param tearoff: メニューウィジェットを独立したウィンドウにするかを指定する
        :type tearoff: bool
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Column(
        layout: list[list] = [[]],
        borderwidth: int | float = 0,
        takefocus: bool = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        bg: ColorTypeN = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        フレームを作成する

        :param layout: Columnウィジェットに表示させるウィジェットを指定する各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます
        :type layout: list[list]
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Slidebar(
        value: int | float = 0,
        digits: int = 0,
        resolution: int | float = 1,
        length: int | float = 200,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        min: int | float = 0,
        max: int | float = 100,
        borderwidth: int | float = 1,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        スライダーを作成する

        :param value: Slidebarウィジェットの読み込み時の初期値を指定する
        :type value: int | float
        :param digits: スケールの値を文字列として取得した際の数値の最大桁数を指定する
        :type digits: int
        :param resolution: スライダーのステップ数を指定する
        :type resolution: int | float
        :param length: Slidebarウィジェットの長さを指定する
        :type length: int | float
        :param orientation: Slidebarウィジェットの向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param min: Slidebarウィジェットの数値の最小値を指定する
        :type min: int | float
        :param max: Slidebarウィジェットの数値の最大値を指定する
        :type max: int | float
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def InputNumber(
        values: int | float = 0,
        min: int | float = 0,
        max: int | float = 100,
        takefocus: bool = ...,
        cursor: _Cursor = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        insertwidth: int | float = 2,
        insertbg: ColorTypeN = "#000000",
        step: int | float = 1,
        width: int | float = 20,
        wrap: bool = False,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        bg: ColorTypeN = "#e0e0e0",
        fg: ColorTypeN = ...,
        borderwidth: int | float = 0,
        justify: Literal["left", "center", "right"] = "left",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        数値専用の入力欄を作成する

        :param wrap: 数値が`max`もしくは`min`で指定した範囲外を選択しようとした場合,`max`より大きい数値の場合は`min`へ`min`より小さい数値の場合は`max`へ移動するかを指定する
        :type wrap: bool
        :param insertwidth: InputNumberウィジェットの入力時の挿入ポイントの幅を指定する
        :type insertwidth: int | float
        :param insertbg: InputNumberウィジェットの入力時の挿入ポイントの色を指定する
        :type insertbg: ColorTypeN
        :param step: スライダーのステップ数を指定する
        :type step: int | float
        :param min: Slidebarウィジェットの数値の最小値を指定する
        :type min: int | float
        :param max: Slidebarウィジェットの数値の最大値を指定する
        :type max: int | float
        :param values: Slidebarウィジェットの読み込み時の初期値を指定する
        :type values: int | float
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def FileLoad(
        text: str = "select File",
        title: str = "select File",
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        width: int | float | None = ...,
        height: int | float | None = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        bg: ColorTypeN = "#e0e0e0",
        fg: ColorTypeN = ...,
        takefocus: bool = ...,
        justify: Literal["left", "center", "right"] = "left",
        wraplength: int | float = 0,
        borderwidth: int | float = 0,
        anchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "center",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ファイルパスを取得するダイアログを発生させるボタンを作成する

        :param text: FileLoadウィジェットのボタンに表示させる文字を指定する
        :type text: str
        :param title: ファイルを選択するダイアログのタイトルを指定する
        :type title: str
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def FolderLoad(
        text: str = "select Folder",
        title: str = "select Folder",
        wraplength: int | float = 0,
        borderwidth: int | float = 0,
        anchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "center",
        bg: ColorTypeN = "#e0e0e0",
        fg: ColorTypeN = ...,
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        width: int | float | None = ...,
        height: int | float | None = ...,
        justify: Literal["left", "center", "right"] = "left",
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ファイルパスを取得するダイアログを発生させるボタンを作成する

        :param text: FolderLoadウィジェットのボタンに表示させる文字を指定する
        :type text: str
        :param title: フォルダを選択するダイアログのタイトルを指定する
        :type title: str
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Savebtn(
        initialfile: str = ...,
        initialdir: str = ...,
        filetypes: list[tuple[str, str]] = [("All files", "*.*")],
        defaultextension: str = ".txt",
        text: str = "Save file",
        title: str = "Save file",
        bg: ColorTypeN = "#e0e0e0",
        fg: ColorTypeN = ...,
        justify: Literal["left", "center", "right"] = "left",
        wraplength: int | float = 0,
        borderwidth: int | float = 0,
        anchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "center",
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        width: int | float | None = ...,
        height: int | float | None = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ファイルもしくはフォルダを選択し,選択されたパスを取得するダイアログを発生させるボタンを作成する

        :param text: Savebtnウィジェットのボタンに表示させる文字を指定する
        :type text: str
        :param title: フォルダを選択するダイアログのタイトルを指定する
        :type title: str
        :param filetypes: 保存できるファイル形式の選択肢を指定する
        :type filetypes: list[tuple[str,str]]
        :param initialdir: ダイアログを開く初期ディレクトリを指定する
        :type initialdir: str
        :param initialfile: ファイル名フィールドの初期値を指定する
        :type initialfile: str
        :param defaultextension: 拡張子が設定されていない時のデフォルトを指定する
        :type defaultextension: str
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Colorbtn(
        color: ColorTypeN = "#ffffff",
        text: str = "select color",
        title: str = "select color",
        key: str | None = ...,
        bg: ColorTypeN = "#e0e0e0",
        fg: ColorTypeN = ...,
        justify: Literal["left", "center", "right"] = "left",
        wraplength: int | float = 0,
        borderwidth: int | float = 0,
        anchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "center",
        padx: int | float = ...,
        pady: int | float = ...,
        cursor: _Cursor = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        width: int | float | None = ...,
        height: int | float | None = ...,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = ...,
    ) -> dict[str, Any]:
        """
        色を選択し,選択された色を取得するダイアログを発生させるボタンを作成する

        :param color: ダイアログで選択される色の初期値を選択する
        :type color: ColorTypeN
        :param text: Colorbtnウィジェットのボタンに表示させる文字を指定する
        :type text: str
        :param title: 色を選択するダイアログのタイトルを指定する
        :type title: str
        :param width: ウィジェットの幅を指定する
        :type width: int | float | None
        :param height: ウィジェットの高さを指定する
        :type height: int | float | None
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param borderwidth: ウィジェットの周囲に表示させる枠線の太さを指定する
        :type borderwidth: int | float
        :param padx: ウィジェットの外側の左右に空白を入れるサイズを指定する
        :type padx: int | float
        :param pady: ウィジェットの外側の上下に空白を入れるサイズを指定する
        :type pady: int | float
        :param wraplength: テキストの折り返し幅を指定する
        :type wraplength: int | float
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param justify: 行揃えを行う方向を指定する
        :type justify: Literal["left", "center", "right"]
        :param anchor: ウィジェット内の文字の位置を指定する
        :type anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
        :param relief: ウィジェットの周囲に枠線について指定する
        :type relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Tab(
        tabs: list[list[str, list[list]]] = ...,
        bg: ColorTypeN = ...,
        fg: ColorTypeN = ...,
        family: str = ...,
        font_size: int | float = 14,
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        タブを作成する

        :param tabs: Tabウィジェットに表示させるウィジェットを指定する配列の最初の要素にタブ名を,次の要素にTabウィジェットに表示させる`layout`を指定する
        :type tabs: list[list[str,list[list]]]
        :param bg: ウィジェットの背景色を指定する
        :type bg: ColorTypeN
        :param fg: ウィジェットの文字色を指定する
        :type fg: ColorTypeN
        :param family: ウィジェットに表示させる文字のフォント名を指定する
        :type family: str
        :param font_size: ウィジェットに表示させる文字のフォントサイズを指定する
        :type font_size: int | float
        :param weight: ウィジェットに表示させる文字のフォントの太さを指定する
        :type weight: Literal["normal", "bold"]
        :param slant: ウィジェットに表示させる文字のフォントの斜体にするか指定する
        :type slant: Literal["roman", "italic"]
        :param underline: ウィジェットに表示させる文字のフォントの下線を表示させるかを指定する
        :type underline: bool
        :param overstrike: ウィジェットに表示させる文字のフォントの取り消し線を加えるか指定する
        :type overstrike: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def TProgressbar(
        value: int | float = 0,
        max: int | float = 100,
        length: int | float = 200,
        mode: Literal["determinate", "indeterminate"] = "determinate",
        orient: Literal["horizontal", "vertical"] = "horizontal",
        cursor: _Cursor = ...,
        takefocus: bool = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        プログレスバーを作成する

        :param length: TProgressbarウィジェットの長さを指定する
        :type length: int | float
        :param orient: TProgressbarウィジェットの向きを指定する
        :type orient: Literal["horizontal","vertical"]
        :param mode: 決定的モード(determinate)か非決定的モード(indeterminate)かを指定する
        :type mode: Literal["determinate","indeterminate"]
        :param max: TProgressbarウィジェットの数値の最大値を指定する
        :type max: int | float
        :param value: TProgressbarウィジェットの読み込み時の初期値を指定する
        :type value: int | float
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param cursor: マウスカーソルを指定する
        :type cursor: _Cursor
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Barcode(
        data: str | int,
        fotmat: Literal[
            "codabar",
            "code128",
            "code39",
            "ean",
            "ean13",
            "ean13-guard",
            "ean14",
            "ean8",
            "ean8-guard",
            "gs1",
            "gs1_128",
            "gtin",
            "isbn",
            "isbn10",
            "isbn13",
            "issn",
            "itf",
            "jan",
            "nw-7",
            "pzn",
            "upc",
            "upca",
        ] = "code39",
        takefocus: bool = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        バーコードを作成する

        :param data: バーコードで表示させる値を指定する
        :type data: str | int
        :param format: バーコードの形式を指定する
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        :raises TypeError: `data`にint型もしくはstr型を指定しなかった場合に発生させる
        """

    @staticmethod
    def QRImage(
        text: str = ..., takefocus: bool = ..., key: str | None = ...
    ) -> dict[str, Any]:
        """
        QRコードを作成する

        :param text: QRコードを読み取った際に表示させる値を指定する
        :type text: str
        :param takefocus: キーボードによる移動のときにウィンドウがフォーカスを受け入れるかを指定する
        :type takefocus: bool
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def LineGraph(
        x: TypeArrayLikeNS,
        y: TypeArrayLikeNS,
        linewidth: int | float = 2,
        alpha: int | float = 1,
        markersize: int | float = 10,
        marker: Type_Marker = "none",
        linestyle: Type_Solid = "-",
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        折線グラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNS
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNS
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param linewidth: 折線グラフの線の幅を指定する
        :type linewidth: int | float
        :param markersize: 折線グラフのマーカーの大きさを指定する
        :type markersize: int | float
        :param marker: 折線グラフのマーカーを指定する
        :type marker: Type_Marker
        :param linestyle: 折線グラフの線の種類を指定する
        :type linestyle: Literal["-","--","-.",":","None"," ",""]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def BarGraph(
        x: TypeArrayLikeNS,
        y: TypeArraysLikeNumber,
        logs: bool = False,
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        linewidth: int | float = 2,
        width: int | float = 1,
        align: Literal["center", "edge"] = "center",
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        棒グラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNS
        :param y: `y`のデータを指定する
        :type y: TypeArraysLikeNumber
        :param logs: y軸を対数スケールにするかを指定する
        :type logs: bool
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param linewidth: 折線グラフの線の幅を指定する
        :type linewidth: int | float
        :param width: 棒グラフのバー幅を指定する
        :type width: int | float
        :param align: x軸の棒グラフバーの配置を指定する
        :type align: Literal["center","edge"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def BarhGraph(
        x: TypeArraysLikeNumber,
        y: TypeArrayLikeNS,
        logs: bool = False,
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        linewidth: int | float = 2,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        alpha: int | float = 1,
        height: int | float = 1,
        align: Literal["center", "edge"] = "center",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        横向き棒グラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArraysLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNS
        :param logs: x軸を対数スケールにするかを指定する
        :type logs: bool
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param linewidth: 折線グラフの線の幅を指定する
        :type linewidth: int | float
        :param height: 横向き棒グラフのバーの幅を指定する
        :type height: int | float
        :param align: x軸の横向き棒グラフバーの配置を指定する
        :type align: Literal["center","edge"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Funne(
        data: TypeArraysLikeNumber,
        xmajormaxbins: int = 11,
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        linewidth: int | float = 2,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        alpha: int | float = 1,
        height: int | float = 1,
        align: Literal["center", "edge"] = "center",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        じょうごグラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArraysLikeNumber
        :param xmajormaxbins: x軸の目盛りの数の最大数を指定する2n+1(nは正の整数)の整数を指定する
        :type xmajormaxbins: int
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param linewidth: 折線グラフの線の幅を指定する
        :type linewidth: int | float
        :param height: 棒グラフのバーの幅を指定する
        :type height: int | float
        :param align: x軸の棒グラフバーの配置を指定する
        :type align: Literal["center","edge"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Stacked(
        data: TypeArraysLikeNumber,
        dataname: TypeArraysLikeNS,
        width: int | float = 0.8,
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        積み上げ棒グラフを作成する

        :param data: `data`を指定する
        :type data: TypeArraysLikeNumber
        :param dataname: カテゴリ名を指定する
        :type dataname: TypeArraysLikeNS
        :param width: 積み上げ棒グラフの幅のサイズを指定する
        :type width: int | float
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Stackedh(
        data: TypeArraysLikeNumber,
        dataname: TypeArrayLikeNS,
        height: int | float = 0.8,
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        積み上げ横向き棒グラフを作成する

        :param data: `data`を指定する
        :type data: TypeArraysLikeNumber
        :param dataname: カテゴリ名を指定する
        :type dataname: TypeArrayLikeNS
        :param height: 積み上げ横向き棒グラフの高さのサイズを指定する
        :type height: int | float
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Pie(
        data: TypeArrayLikeNumber,
        startangle: int | float = 0,
        startangletype: bool = True,
        shadow: bool = False,
        counterclock: bool = False,
        labeldistance: int | float = 1.1,
        explode: list[int, float] | tuple[int, float] | int | float = ...,
        label: str | list[str] | None = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        円グラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param startangle: 各要素の出力を開始する角度を指定する
        :type startangle: int | float
        :param startangletype: 各要素の出力を開始する角度を度数法(True)か弧度法(False)かを指定する
        :type startangletype: bool
        :param shadow: 円グラフに影を追加するか指定する
        :type shadow: bool
        :param counterclock: 時計回りで出力するか指定する
        :type counterclock: bool
        :param labeldistance: 中心からラベルの距離を指定する
        :type labeldistance: int | float
        :param explode: 中心から各セグメントの離す距離を指定する
        :type explode: list[int,float] | tuple[int,float] | int | float
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Boxplot(
        data: TypeArraysLikeNumber,
        label: str | list[str] | None = ...,
        legend: bool = False,
        fill: bool = False,
        notch: bool = False,
        showfliers: bool = True,
        orientation: Literal["horizontal", "vertical"] = "vertical",
        width: int | float = 0.15,
        whis: float | tuple[float, float] = 1.5,
        xlabel: str = ...,
        ylabel: str = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        箱ひげ図を作成する

        :param data: `data`のデータを指定する
        :type data: TypeArraysLikeNumber
        :param label: 箱ひげ図のデータ名を指定する指定しなかった場合`box`+データの数になる例)box0,box1
        :type label: str | list[str] | None
        :param legend: 凡例を表示させるか指定する
        :type legend: bool
        :param fill: 箱内を塗りつぶすかを指定する
        :type fill: bool
        :param notch: 箱の中央をくびれさすか指定する
        :type notch: bool
        :param showfliers: 外れ値を表示させるか指定する
        :type showfliers: bool
        :param orientation: 箱ひげ図の向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param whis: ヒゲの位置を指定する
        :type whis: float | tuple[float,float]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Waterfall(
        x: TypeArraysLikeNS,
        y: TypeArrayLikeNumber,
        sums: bool = False,
        sumstext: str = "sum",
        colorline: ColorTypeN = "#4477aa",
        linestyle: Type_Solid = "-",
        ucolor: ColorTypeN = "#156082",
        dcolor: ColorTypeN = "#e97132",
        width: int | float = 1,
        xlabel: str = ...,
        ylabel: str = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        横向き滝グラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArraysLikeNS
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param sums: 合計値を表示するかを指定する
        :type sums: bool
        :param sumstext: 合計のラベルを指定する
        :type sumstext: str
        :param colorline: バーとバーを繋げる線の色を指定する
        :type colorline: ColorTypeN
        :param ucolor: 上昇バーの色を指定する
        :type ucolor: ColorTypeN
        :param dcolor: 下降バーの色を指定する
        :type dcolor: ColorTypeN
        :param width: バーの幅を指定する
        :type width: int | float
        :param linestyle: バーとバーを繋げる線の種類を指定する
        :type linestyle: Literal["-","--","-.",":","None"," ",""]
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Waterfallh(
        x: TypeArraysLikeNS,
        y: TypeArrayLikeNumber,
        sums: bool = False,
        sumstext: str = "sum",
        colorline: ColorTypeN = "#4477aa",
        linestyle: Type_Solid = "-",
        ucolor: ColorTypeN = "#156082",
        dcolor: ColorTypeN = "#e97132",
        height: int | float = 1,
        xlabel: str = ...,
        ylabel: str = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        y軸向きにバーを設置された滝グラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArraysLikeNS
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param sums: 合計値を表示するかを指定する
        :type sums: bool
        :param sumstext: 合計のラベルを指定する
        :type sumstext: str
        :param colorline: バーとバーを繋げる線の色を指定する
        :type colorline: ColorTypeN
        :param linestyle: バーとバーを繋げる線の種類を指定する
        :type linestyle: Literal["-","--","-.",":","None"," ",""]
        :param ucolor: 上昇バーの色を指定する
        :type ucolor: ColorTypeN
        :param dcolor: 下降バーの色を指定する
        :type dcolor: ColorTypeN
        :param height: バーの幅を指定する
        :type height: int | float
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Scatter(
        x: TypeArraysLikeNS,
        y: TypeArraysLikeNS,
        marker: Type_Marker = "o",
        markersize: int | float = 10,
        regression_bool: bool = False,
        linestyle: Type_Solid = "-",
        linewidth: int | float = 2,
        xlabel: str = ...,
        ylabel: str = ...,
        label: str | list[str] | None = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        散布図を作成する

        :param x: `x`のデータを指定する
        :type x: TypeArraysLikeNS
        :param y: `y`のデータを指定する
        :type y: TypeArraysLikeNS
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param marker: 散布図のマーカーを指定する
        :type marker: Type_Marker
        :param markersize: 散布図のマーカーの大きさを指定する
        :type markersize: int | float
        :param regression_bool: 散布図に回帰直線を描画させるか指定する
        :type regression_bool: bool
        :param linestyle: 散布図に回帰直線の線の種類を指定する
        :type linestyle: Type_Solid
        :param linewidth: 散布図に回帰直線の線の太さを指定する
        :type linewidth: int | float
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def DScatter(
        x: TypeArraysLikeNS,
        y: TypeArraysLikeNS,
        z: TypeArraysLikeNS,
        xlabel: str = ...,
        ylabel: str = ...,
        zlabel: str = ...,
        marker: Type_Marker = "o",
        markersize: int | float = 10,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xyz: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        grid_z: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        zmajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        zticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        znumticks: int | float | None = None,
        mouse_rotation: bool = True,
        elev: int | float = 30,
        azim: int | float = 45,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        立体散布図を作成する

        :param x: `x`のデータを指定する
        :type x: TypeArraysLikeNS
        :param y: `y`のデータを指定する
        :type y: TypeArraysLikeNS
        :param z: `z`のデータを指定する
        :type z: TypeArraysLikeNS
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param zlabel: z軸のラベルを指定する
        :type zlabel: str
        :param marker: 散布図のマーカーを指定する
        :type marker: Type_Marker
        :param markersize: 散布図のマーカーの大きさを指定する
        :type markersize: int | float
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xyz: x軸,y軸,z軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`,`grid_z`より優先度が高い
        :type grid_xyz: bool
        :param grid_x: x軸にグリッド線を表示させるか指定する`grid_xyz`より優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定する`grid_xyz`より優先度が低い
        :type grid_y: bool
        :param grid_z: z軸にグリッド線を表示させるか指定する`grid_xyz`より優先度が低い
        :type grid_z: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param zticksrange: z軸の目盛の範囲を変更する
        :type zticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param zmajorint: z軸の目盛りを整数で自動調整させるか指定する
        :type zmajorint: bool
        :param ticksshow: x軸,y軸,z軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param zticksshow: z軸のグリッド線と目盛り値について表示するかを指定する
        :type zticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param znumticks: z軸の目盛りの数を指定する
        :type znumticks: int | float | None
        :param mouse_rotation: 表示されているグラフをマウスで操作できるか指定する
        :type mouse_rotation: bool
        :param elev: 仰角を度数表記で指定する
        :type elev: int | float
        :param azim: 方位角を度数表記で指定する
        :type azim: int | float
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Stem(
        x: TypeArrayLikeNumber = ...,
        y: TypeArrayLikeNumber = ...,
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        orientation: Literal["horizontal", "vertical"] = "vertical",
        bottom: int | float = 0,
        linefmt: str | None = ...,
        markerfmt: str | None = ...,
        basefmt: str | None = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        幹図を作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param orientation: 茎の向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param bottom: ベースラインの位置を指定する
        :type bottom: int | float
        :param linefmt: 垂直線の色や線種を指定する
        :type linefmt: str | None
        :param markerfmt: 茎の先端にあるマーカーの色や形状を指定する
        :type markerfmt: str | None
        :param basefmt: ベースラインのプロパティを指定する
        :type basefmt: str | None
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Step(
        data: TypeArraysLikeNumber,
        fill: bool = False,
        baseline: int | float = 0,
        orientation: Literal["horizontal", "vertical"] = "vertical",
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        label: str | list[str] | None = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        階段グラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArraysLikeNumber
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param baseline: 階段の下端の開始位置を指定する
        :type baseline: int | float
        :param fill: 階段の下部から`baseline`の間を塗りつぶすかを指定する
        :type fill: bool
        :param orientation: グラフの向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する
        :type y_verwrit: Literal["horizontal","vertical"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Hatplot(
        x: TypeArrayLikeNumber,
        data: TypeArrayLikeNumber,
        color: ColorTypeN = "#4477aa",
        xlabel: str = ...,
        ylabel: str = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ハットグラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Hist(
        data: TypeArrayLikeNumber,
        label: str | list[str] | None = ...,
        width: int | float = 1,
        min: int | float = ...,
        max: int | float = ...,
        orientation: Literal["horizontal", "vertical"] = "vertical",
        bottom: int | float = 0,
        bins: (
            int
            | ArrayLike
            | Literal[
                "auto", "fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"
            ]
        ) = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        xlabel: str = ...,
        ylabel: str = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        ヒストグラムを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param width: ヒストグラムのバーのサイズを指定する
        :type width: int | float
        :param orientation: ヒストグラムの向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param bottom: ヒストグラムのバーの位置を指定する
        :type bottom: int | float
        :param min: ヒストグラムで表示される最小値を指定する
        :type min: int | float
        :param max: ヒストグラムで表示される最大値を指定する
        :type max: int | float
        :param bins: `bins`を指定する
        :type bins: int | ArrayLike | Literal["auto","fd","doane","scott","stone","rice","sturges","sqrt"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する
        :type y_verwrit: Literal["horizontal","vertical"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Stack(
        x: TypeArrayLikeNS,
        y: TypeArraysLikeNumber,
        hatch: str | None = None,
        baseline: Literal["zero", "sym", "wiggle", "weighted_wiggle"] = "zero",
        xlabel: str = ...,
        ylabel: str = ...,
        label: str | list[str] | None = ...,
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        積み上げエリアチャートを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNS
        :param y: `y`のデータを指定する
        :type y: TypeArraysLikeNumber
        :param hatch: 塗りつぶし領域内の模様を指定する
        :type hatch: str | None
        :param baseline: 基準値の算出方法を指定する
        :type baseline: Literal["zero","sym","wiggle","weighted_wiggle"]
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Linefill(
        x: TypeArrayLikeNumber,
        ymin: TypeArrayLikeNumber = ...,
        ymax: TypeArrayLikeNumber = ...,
        centerlinewidth: int | float = 2,
        alpha: int | float = 0.5,
        xlabel: str = ...,
        ylabel: str = ...,
        label: str | list[str] | None = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        積上げ面グラフを作成する

        :param x: 曲線を定義する節点のx座標を指定する
        :type x: TypeArrayLikeNumber
        :param ymin: 最初の曲線を定義する節点のy座標を指定する
        :type ymin: TypeArrayLikeNumber
        :param ymax: 2つ目の曲線を定義する節点のy座標を指定する
        :type ymax: TypeArrayLikeNumber
        :param centerlinewidth: 線の太さを指定する
        :type centerlinewidth: int | float
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Ecdf(
        data: TypeArraysLikeNumber,
        complementary: bool = False,
        compress: bool = False,
        orientation: Literal["horizontal", "vertical"] = "vertical",
        linestyle: Type_Solid = "-",
        linewidth: int | float = 1.5,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        経験的累積分布関数を作成する

        :param data: 入力データを指定する
        :type data: TypeArraysLikeNumber
        :param complementary: 補累積分布を描画するか指定する
        :type complementary: bool
        :param compress: 同一値のデータをまとめて最適化するかどうか指定する
        :type compress: bool
        :param orientation: プロットの向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param linestyle: 線の種類を指定する
        :type linestyle: Literal["-","--","-.",":","None"," ",""]
        :param linewidth: 線の太さを指定する
        :type linewidth: int | float
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Errorbar(
        x: TypeArraysLikeNumber,
        y: TypeArraysLikeNumber,
        err: TypeArrayLikeNumber = ...,
        xerr: TypeArrayLikeNumber = ...,
        yerr: TypeArrayLikeNumber = ...,
        xuplims: bool = False,
        xlolims: bool = False,
        yuplims: bool = False,
        ylolims: bool = False,
        barsabove: bool = False,
        linewidth: int | float = 1.5,
        capthick: int | float = 10,
        capsize: int | float = 0,
        errorevery: int | tuple[int, ...] = 1,
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        xlabel: str = ...,
        ylabel: str = ...,
        label: str | list[str] | None = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        誤差範囲付きの線グラフもしくはマーカーグラフ,あるいはその両方のエラーグラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArraysLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArraysLikeNumber
        :param err: `x`と`y`のデータの誤差の配列を指定する
        :type err: TypeArrayLikeNumber
        :param xerr: `x`のデータの誤差の配列を指定する
        :type xerr: TypeArrayLikeNumber
        :param yerr: `y`のデータの誤差の配列を指定する
        :type yerr: TypeArrayLikeNumber
        :param xuplims: `x`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type xuplims: bool
        :param xlolims: `x`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type xlolims: bool
        :param yuplims: `y`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type yuplims: bool
        :param ylolims: `y`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type ylolims: bool
        :param barsabove: 誤差範囲をグラフ記号の上に表示させるか指定する
        :type barsabove: bool
        :param linewidth: データ点を結ぶ線の太さを指定する
        :type linewidth: int | float
        :param capthick: キャップの厚みを指定する
        :type capthick: int | float
        :param capsize: エラーバーの先端にあるキャップの長さを指定する
        :type capsize: int | float
        :param errorevery: エラーバーを表示する頻度を指定する
        :type errorevery: int | tuple[int,...]
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Eventplot(
        data: TypeArrayLikeNumber,
        linewidth: int | float = 1,
        linelength: int | float = 1,
        linestyle: Type_Solid | tuple[Type_Solid, ...] = "-",
        orientation: Literal["horizontal", "vertical"] = "vertical",
        xlabel: str = ...,
        ylabel: str = ...,
        label: str | list[str] | None = ...,
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksshow: bool = False,
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        イベントグラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param linewidth: イベントグラフの線の太さを指定する
        :type linewidth: int | float
        :param linelength: 線の合計の高さを指定する
        :type linelength: int | float
        :param linestyle: 線の種類を指定する
        :type linestyle: Literal["-","--","-.",":","None"," ",""] | tuple[Literal["-","--","-.",":","None"," ",""],...]
        :param orientation: 向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Hist2d(
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNumber,
        max: int | float = ...,
        min: int | float = ...,
        xmax: int | float = ...,
        xmin: int | float = ...,
        ymax: int | float = ...,
        ymin: int | float = ...,
        bins: int | tuple[int, int] | ArrayLike | tuple[ArrayLike, ArrayLike] = 10,
        density: bool = False,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksdirection: Literal["out", "in", "inout"] = "out",
        xlabel: str = ...,
        ylabel: str = ...,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        2次元ヒストグラムを作成する

        :param x: `x`のデータを一次元配列で指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを一次元配列で指定する
        :type y: TypeArrayLikeNumber
        :param max,min: 表示させたいカウントの範囲を指定する
        :type max,min: int | float
        :param xmax,xmin: x軸の`bins`の範囲を指定する
        :type xmax,xmin: int | float
        :param ymax,ymin: y軸の`bins`の範囲を指定する
        :type ymax,ymin: int | float
        :param bins: ビンの数を指定する
        :type bins: int | tuple[int,int] | ArrayLike | tuple[ArrayLike,ArrayLike]
        :param density: ヒストグラムを正規化かするかを指定する
        :type density: bool
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :raises TypeError: `x`もしくは`y`もしくはその両方が二次元配列以上の多次元配列の場合に発生させる
        :raises TypeError: `x`と`y`の要素の数が同じではない時に発生させる
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Violinplot(
        self,
        data: TypeArraysLikeNumber,
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNumber,
        orientation: Literal["horizontal", "vertical"] = "vertical",
        width: int | float = 1,
        alpha: int | float = 1,
        showextrema: bool = True,
        showmeans: bool = False,
        showmedians: bool = False,
        points: int | float = 100,
        bw_method: (
            Literal["scott", "silverman"] | float | Callable[[GaussianKDE], float]
        ) = "scott",
        side: Literal["both", "low", "high"] = "both",
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksshow: bool = False,
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        バイオリングラフを作成する

        :param data: 入力データを指定する
        :type data: TypeArraysLikeNumber
        :param x: `orientation`が`vertical`の時にx軸上にバイオリンが設置される配列を指定する
        :type x: TypeArraysLikeNumber
        :param y: `orientation`が`horizontal`の時にy軸上にバイオリンが設置される配列を指定する
        :type y: TypeArraysLikeNumber
        :param orientation: バイオリンが設置される軸の向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param width: バイオリンの幅を指定する
        :type width: int | float
        :param showextrema: 極値を線で示すか指定する
        :type showextrema: bool
        :param showmeans: 平均値を線で示すかどうか指定する
        :type showmeans: bool
        :param showmedians: 中央値を線で示すかどうか指定する
        :type showmedians: bool
        :param points: 各ガウスカーネル密度推定値を評価する点の数を指定する
        :type points: int | float
        :param bw_method: 推定器の帯域幅を計算するために使用されるメソッドを指定する
        :type bw_method: Literal["scott","silverman"] | float | Callable[[GaussianKDE],float]
        :param side: バイオリンの左右対称もしくは左右(上下)のみを描画するか指定する
        :type side: Literal["both","low","high"]
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def Hexbin(
        self,
        x: TypeArrayLikeNumber,
        y: TypeArrayLikeNumber,
        c: TypeArrayLikeNumber | None = None,
        gridsize: int | tuple[int, int] = 100,
        extent: tuple[int | float, int | float, int | float, int | float] | None = None,
        xscale: Literal["linear", "log"] = "linear",
        yscale: Literal["linear", "log"] = "linear",
        mincnt: int = 1,
        bins: Literal["log"] | int | tuple[float, ...] | None = None,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        title: str = ...,
        dpi: int | float = 100,
        alpha: int | float = 1,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        xticksdirection: Literal["out", "in", "inout"] = "out",
        yticksshow: bool = False,
        yticksdirection: Literal["out", "in", "inout"] = "out",
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        2次元六角形ビニンググラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param c: 各ポイントの値を指定する
        :type c: TypeArrayLikeNumber
        :param gridsize: `bins`の細かさを指定する
        :type gridsize: int | tuple[int,int]
        :param extent: 各ポイントの値を指定する
        :type extent: tuple[int|float,int|float,int|float,int|float] | None
        :param xscale,yscale: 軸のスケールを指定する
        :type xscale,yscale: Literal["linear","log"]
        :param mincnt: 描画する`bins`の最小カウント数を指定する
        :type mincnt: int
        :param bins: ビンのカウント方法を指定する
        :type bins: Literal["log"] | int | tuple[float,...] | None
        :param xlabel: x軸のラベルを指定する
        :type xlabel: str
        :param ylabel: y軸のラベルを指定する
        :type ylabel: str
        :param label: ラベルを指定する
        :type label: str | list[str] | None
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Barpolar(
        x: TypeArrayLikeNumber = ...,
        y: TypeArrayLikeNumber = ...,
        align: Literal["center", "edge"] = "center",
        width: int | float = 1,
        alpha: int | float = 1,
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸棒グラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArraysLikeNumber
        :param width: 棒グラフのバー幅を指定する
        :type width: int | float
        :param align: x軸の棒グラフバーの配置を指定する
        :type align: Literal["center","edge"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Barpolar(
        data: TypeArrayLikeNumber = ...,
        align: Literal["center", "edge"] = "center",
        width: int | float = 1,
        alpha: int | float = 1,
        color: ColorTypeN | tuple[ColorTypeN, ...] = ...,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸棒グラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArraysLikeNumber
        :param width: 棒グラフのバー幅を指定する
        :type width: int | float
        :param align: x軸の棒グラフバーの配置を指定する
        :type align: Literal["center","edge"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param color: 色を指定する
        :type color: ColorTypeN | tuple[ColorTypeN,...]
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Stempolar(
        x: TypeArrayLikeNumber = ...,
        y: TypeArrayLikeNumber = ...,
        linefmt: str | None = None,
        markerfmt: str | None = None,
        basefmt: str | None = None,
        bottom: int | float = 0,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸幹図を作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param linefmt: 垂直線の色や線を指定する
        :type linefmt: str | None
        :param markerfmt: 茎の先端にあるマーカーの色や形状を指定する
        :type markerfmt: str | None
        :param basefmt: ベースラインのプロパティを指定する
        :type basefmt: str | None
        :param bottom: ベースラインの座標を指定する
        :type bottom: int | float
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Stempolar(
        data: TypeArrayLikeNumber = ...,
        linefmt: str | None = None,
        markerfmt: str | None = None,
        basefmt: str | None = None,
        bottom: int | float = 0,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸幹図を作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param linefmt: 垂直線の色や線を指定する
        :type linefmt: str | None
        :param markerfmt: 茎の先端にあるマーカーの色や形状を指定する
        :type markerfmt: str | None
        :param basefmt: ベースラインのプロパティを指定する
        :type basefmt: str | None
        :param bottom: ベースラインの座標を指定する
        :type bottom: int | float
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Errorpolar(
        x: TypeArrayLikeNumber = ...,
        y: TypeArrayLikeNumber = ...,
        err: TypeArrayLikeNumber = ...,
        xerr: TypeArrayLikeNumber = ...,
        yerr: TypeArrayLikeNumber = ...,
        xuplims: bool = False,
        xlolims: bool = False,
        yuplims: bool = False,
        ylolims: bool = False,
        barsabove: bool = False,
        linewidth: int | float = 1.5,
        capthick: int | float = 10,
        capsize: int | float = 0,
        errorevery: int | list[int] | tuple[int] = 1,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸エラーグラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param err: `x`と`y`のデータの誤差の配列を指定する
        :type err: TypeArrayLikeNumber
        :param xerr: `x`のデータの誤差の配列を指定する
        :type xerr: TypeArrayLikeNumber
        :param yerr: `y`のデータの誤差の配列を指定する
        :type yerr: TypeArrayLikeNumber
        :param xuplims: `x`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type xuplims: bool
        :param xlolims: `x`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type xlolims: bool
        :param yuplims: `y`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type yuplims: bool
        :param ylolims: `y`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type ylolims: bool
        :param barsabove: 誤差範囲をグラフ記号の上に表示させるか指定する
        :type barsabove: bool
        :param linewidth: データ点を結ぶ線の太さを指定する
        :type linewidth: int | float
        :param capthick: キャップの厚みを指定する
        :type capthick: int | float
        :param capsize: エラーバーの先端にあるキャップの長さを指定する
        :type capsize: int | float
        :param errorevery: エラーバーを表示する頻度を指定する
        :type errorevery: int | list[int] | tuple[int]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Errorpolar(
        data: TypeArrayLikeNumber = ...,
        err: TypeArrayLikeNumber = ...,
        xerr: TypeArrayLikeNumber = ...,
        yerr: TypeArrayLikeNumber = ...,
        xuplims: bool = False,
        xlolims: bool = False,
        yuplims: bool = False,
        ylolims: bool = False,
        barsabove: bool = False,
        linewidth: int | float = 1.5,
        capthick: int | float = 10,
        capsize: int | float = 0,
        errorevery: int | list[int] | tuple[int] = 1,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸エラーグラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param err: `x`と`y`のデータの誤差の配列を指定する
        :type err: TypeArrayLikeNumber
        :param xerr: `x`のデータの誤差の配列を指定する
        :type xerr: TypeArrayLikeNumber
        :param yerr: `y`のデータの誤差の配列を指定する
        :type yerr: TypeArrayLikeNumber
        :param xuplims: `x`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type xuplims: bool
        :param xlolims: `x`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type xlolims: bool
        :param yuplims: `y`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type yuplims: bool
        :param ylolims: `y`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する
        :type ylolims: bool
        :param barsabove: 誤差範囲をグラフ記号の上に表示させるか指定する
        :type barsabove: bool
        :param linewidth: データ点を結ぶ線の太さを指定する
        :type linewidth: int | float
        :param capthick: キャップの厚みを指定する
        :type capthick: int | float
        :param capsize: エラーバーの先端にあるキャップの長さを指定する
        :type capsize: int | float
        :param errorevery: エラーバーを表示する頻度を指定する
        :type errorevery: int | list[int] | tuple[int]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Linepolar(
        x: TypeArrayLikeNumber = ...,
        y: TypeArrayLikeNumber = ...,
        linewidth: int | float = 2,
        markersize: int | float = 10,
        marker: Type_Marker = "",
        linestyle: Type_Solid = "-",
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸折線グラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param linewidth: 極軸折線グラフの線の幅を指定する
        :type linewidth: int | float
        :param markersize: 極軸折線グラフのマーカーの大きさを指定する
        :type markersize: int | float
        :param marker: 折線グラフのマーカーを指定する
        :type marker: Type_Marker
        :param linestyle: 折線グラフの線の種類を指定する
        :type linestyle: Literal["solid","-","dashed","--","dash-dot","-.","dotted",": ","none",None," ",""]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Linepolar(
        data: TypeArrayLikeNumber = ...,
        linewidth: int | float = 2,
        markersize: int | float = 10,
        marker: Type_Marker = None,
        linestyle: Type_Solid = "-",
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸折線グラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param linewidth: 極軸折線グラフの線の幅を指定する
        :type linewidth: int | float
        :param markersize: 極軸折線グラフのマーカーの大きさを指定する
        :type markersize: int | float
        :param marker: 折線グラフのマーカーを指定する
        :type marker: Type_Marker
        :param linestyle: 折線グラフの線の種類を指定する
        :type linestyle: Literal["solid","-","dashed","--","dash-dot","-.","dotted",": ","none",None," ",""]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Eventpolar(
        x: TypeArrayLikeNumber = ...,
        y: TypeArrayLikeNumber = ...,
        linewidth: int | float = 1,
        linelength: int | float = 1,
        linestyle: Type_Solid = "-",
        orientation: Literal["horizontal", "vertical"] = "vertical",
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸イベントグラフを作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param linewidth: イベントグラフの線の太さを指定する
        :type linewidth: int | float
        :param linelength: 線の合計の高さを指定する
        :type linelength: int | float
        :param linestyle: 線の種類を指定する
        :type linestyle: Literal["-","--","-.",":","None"," ",""]
        :param orientation: 向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Eventpolar(
        data: TypeArrayLikeNumber = ...,
        linewidth: int | float = 1,
        linelength: int | float = 1,
        linestyle: Type_Solid = "-",
        orientation: Literal["horizontal", "vertical"] = "vertical",
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸イベントグラフを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param linewidth: イベントグラフの線の太さを指定する
        :type linewidth: int | float
        :param linelength: 線の合計の高さを指定する
        :type linelength: int | float
        :param linestyle: 線の種類を指定する
        :type linestyle: Literal["-","--","-.",":","None"," ",""]
        :param orientation: 向きを指定する
        :type orientation: Literal["horizontal","vertical"]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Scatterpolar(
        x: TypeArrayLikeNumber = ...,
        y: TypeArrayLikeNumber = ...,
        marker: Type_Marker = "o",
        markersize: int | float = 10,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸散布図を作成する

        :param x: `x`のデータを指定する
        :type x: TypeArrayLikeNumber
        :param y: `y`のデータを指定する
        :type y: TypeArrayLikeNumber
        :param marker: 極軸散布図のマーカーを指定する
        :type marker: Type_Marker
        :param markersize: 極軸散布図のマーカーの大きさを指定する
        :type markersize: int | float
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @overload
    @staticmethod
    def Scatterpolar(
        data: TypeArrayLikeNumber = ...,
        marker: Type_Marker = "o",
        markersize: int | float = 10,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        極軸散布図を作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param marker: 極軸散布図のマーカーを指定する
        :type marker: Type_Marker
        :param markersize: 極軸散布図のマーカーの大きさを指定する
        :type markersize: int | float
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def RadarLine(
        data: TypeArrayLikeNumber = ...,
        markersize: int | float = 10,
        marker: Type_Marker = "none",
        linestyle: Type_Solid = "-",
        linewidth: int | float = 2,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        折線レーダーチャートを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param linewidth: 折線グラフの線の幅を指定する
        :type linewidth: int | float
        :param markersize: 折線グラフのマーカーの大きさを指定する
        :type markersize: int | float
        :param marker: 折線グラフのマーカーを指定する
        :type marker: Type_Marker
        :param linestyle: 折線グラフの線の種類を指定する
        :type linestyle: Literal["solid","-","dashed","--","dash-dot","-.","dotted",": ","none",None," ",""]
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @staticmethod
    def RadarFill(
        data: TypeArrayLikeNumber = ...,
        alpha: int | float = 1,
        size: tuple[int | float, int | float] = (500, 400),
        fg: ColorTypeN = "#000000",
        bg: ColorTypeN = "#ffffff",
        title: str = ...,
        dpi: int | float = 100,
        graph_grid: ColorTypeN = "#b7b7b7",
        grid_xy: bool = True,
        grid_x: bool = False,
        grid_y: bool = False,
        tight_layout: bool = True,
        xticksrange: int | float | tuple[int | float, ...] = 0,
        yticksrange: int | float | tuple[int | float, ...] = 0,
        xmajorint: bool = True,
        ymajorint: bool = True,
        ticksshow: bool = False,
        xticksshow: bool = False,
        yticksshow: bool = False,
        key: str | None = ...,
    ) -> dict[str, Any]:
        """
        塗りつぶしレーダーチャートを作成する

        :param data: `data`のデータを指定する
        :type data: TypeArrayLikeNumber
        :param title: グラフのタイトルを指定する
        :type title: str
        :param size: 表示させるグラフの大きさを指定する
        :type size: tuple[int | float,int | float]
        :param fg: グラフ内の文字色を指定する
        :type fg: ColorTypeN
        :param bg: グラフ内の背景色を指定する
        :type bg: ColorTypeN
        :param dpi: 1インチあたりのドット数を指定する
        :type dpi: int | float
        :param alpha: グラフの透明度を指定する
        :type alpha: int | float
        :param graph_grid: グラフのグリッド線の色を指定する
        :type graph_grid: ColorTypeN
        :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する`grid_x`,`grid_y`より優先度が高い
        :type grid_xy: bool
        :param grid_x: x軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_x: bool
        :param grid_y: y軸にグリッド線を表示させるか指定するgrid_xyより優先度が低い
        :type grid_y: bool
        :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する
        :type tight_layout: bool
        :param xticksrange: x軸の目盛の範囲を変更する
        :type xticksrange: int | float | tuple[int | float,...]
        :param yticksrange: y軸の目盛の範囲を変更する
        :type yticksrange: int | float | tuple[int | float,...]
        :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する
        :type xmajorint: bool
        :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する
        :type ymajorint: bool
        :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する
        :type ticksshow: bool
        :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する
        :type xticksshow: bool
        :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する
        :type yticksshow: bool
        :param xticksdirection: x軸の目盛りの向きを指定する
        :type xticksdirection: Literal["out","in","inout"]
        :param yticksdirection: y軸の目盛りの向きを指定する
        :type yticksdirection: Literal["out","in","inout"]
        :param key: ウィジェット固有の番号を指定する
        :type key: str | None
        """

    @classmethod
    def Popup(
        cls,
        title: str = "Information",
        message: str = "Information message",
        icon: Literal["info", "warning", "error", "question"] = "info",
    ) -> Literal["ok"]:
        """
        指定されたタイトルとメッセージを持つ情報メッセージボックスを表示させる

        :param title: 情報メッセージボックスに表示させるタイトル名を指定する
        :type title: str
        :param message: 情報メッセージボックスに表示させるメッセージを指定する
        :type message: str
        :param icon: 情報メッセージボックスに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: Literal["ok"]
        """

    @classmethod
    def Popupwarning(
        cls,
        title: str = "Warning",
        message: str = "Warning message",
        icon: Literal["info", "warning", "error", "question"] = "warning",
    ) -> Literal["ok"]:
        """
        指定されたタイトルとメッセージを含む警告メッセージボックスを表示させる

        :param title: 警告メッセージボックスに表示させるタイトル名を指定する
        :type title: str
        :param message: 警告メッセージボックスに表示させるメッセージを指定する
        :type message: str
        :param icon: 警告メッセージボックスに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: Literal["ok"]
        """

    @classmethod
    def Popupwarningyesno(
        cls,
        title: str = "Warning",
        message: str = "Warning message",
        icon: Literal["info", "warning", "error", "question"] = "warning",
    ) -> Literal["yes", "no"]:
        """
        指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つ警告メッセージボックスを表示させる

        :param title: 警告メッセージボックスに表示させるタイトル名を指定する
        :type title: str
        :param message: 警告メッセージボックスに表示させるメッセージを指定する
        :type message: str
        :param icon: 警告メッセージボックスに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: Literal["yes", "no"]
        """

    @classmethod
    def Popuperror(
        cls,
        title: str = "Error",
        message: str = "Error message",
        icon: Literal["info", "warning", "error", "question"] = "error",
    ) -> Literal["ok"]:
        """
        指定されたタイトルとメッセージを持つエラーメッセージボックスを表示させる

        :param title: エラーメッセージボックスに表示させるタイトル名を指定する
        :type title: str
        :param message: エラーメッセージボックスに表示させるメッセージを指定する
        :type message: str
        :param icon: エラーメッセージボックスに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: Literal["ok"]
        """

    @classmethod
    def Popuperroryesno(
        cls,
        title: str = "Error",
        message: str = "Error message",
        icon: Literal["info", "warning", "error", "question"] = "error",
    ) -> Literal["yes", "no"]:
        """
        指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つエラーメッセージボックスを表示させる

        :param title: エラーメッセージボックスに表示させるタイトル名を指定する
        :type title: str
        :param message: エラーメッセージボックスに表示させるメッセージを指定する
        :type message: str
        :param icon: エラーメッセージボックスに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: Literal["yes", "no"]
        """

    @classmethod
    def Popupquestion(
        cls,
        title: str = "Question",
        message: str = "Question message",
        icon: Literal["info", "warning", "error", "question"] = "question",
    ) -> Literal["yes", "no"]:
        """
        「はい(Yes)」と「いいえ(No)」を選択させるダイアログを表示させる

        :param title: ダイアログに表示させるタイトル名を指定する
        :type title: str
        :param message: ダイアログに表示させるメッセージを指定する
        :type message: str
        :param icon: ダイアログに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: Literal["yes", "no"]
        """

    @classmethod
    def Popupokcancel(
        cls,
        title: str = "Question",
        message: str = "Question message",
        icon: Literal["info", "warning", "error", "question"] = "question",
    ) -> bool:
        """
        「OK」と「キャンセル」を選択させるダイアログを表示させる

        :param title: ダイアログに表示させるタイトル名を指定する
        :type title: str
        :param message: ダイアログに表示させるメッセージを指定する
        :type message: str
        :param icon: ダイアログに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: bool
        """

    @classmethod
    def Popupyesno(
        cls,
        title: str = "Question",
        message: str = "Question message",
        icon: Literal["info", "warning", "error", "question"] = "question",
    ) -> bool:
        """
        「はい(Yes)」と「いいえ(No)」を選択させるダイアログを表示させる

        :param title: ダイアログに表示させるタイトル名を指定する
        :type title: str
        :param message: ダイアログに表示させるメッセージを指定する
        :type message: str
        :param icon: ダイアログに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: Literal["ok"]
        """

    @classmethod
    def Popupyesnocancel(
        cls,
        title: str = "Question",
        message: str = "Question message",
        icon: Literal["info", "warning", "error", "question"] = "question",
    ) -> bool | None:
        """
        「はい(Yes)」、「いいえ(No)」、「キャンセル(Cancel)」を選択させるダイアログを表示させる

        :param title: ダイアログに表示させるタイトル名を指定する
        :type title: str
        :param message: ダイアログに表示させるメッセージを指定する
        :type message: str
        :param icon: ダイアログに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: bool | None
        """

    @classmethod
    def Popuptry(
        cls,
        title: str = "Question",
        message: str = "Question message",
        icon: Literal["info", "warning", "error", "question"] = "question",
    ) -> bool:
        """
        操作を再試行するかどうかを尋ねる「再試行」と「キャンセル」が設置されたダイアログを表示させる

        :param title: ダイアログに表示させるタイトル名を指定する
        :type title: str
        :param message: ダイアログに表示させるメッセージを指定する
        :type message: str
        :param icon: ダイアログに表示させるアイコンを指定する
        :type icon: Literal["info","warning","error","question"]
        :return: ポップアップの返答を返す
        :rtype: bool
        """
