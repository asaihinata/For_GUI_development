from tkinter import Label
from typing import Any, Literal

from PIL.ImageTk import PhotoImage

from ....base import _Element

__all__ = ["Barcode"]

class Barcode(_Element):
    imgs: PhotoImage
    widget: Label
    def delta(self) -> None:
        """ウィジェットを削除する"""

    def show(self, title: str | None = None) -> None:
        """
        画像を表示させる

        :param title: タイトルを指定する
        :type title: str | None
        """

class barcode_data:
    def __init__(
        self,
        value: Any,
        format: Literal[
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
    ) -> None: ...
    def get_type(self) -> str: ...
