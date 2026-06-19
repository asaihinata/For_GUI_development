"""フォントを設定するモジュール"""

from tkinter import Misc, Tk
from tkinter.font import Font, families

from ..dev import bols, listchose
from ..readfile import Getfont

__all__ = ["TKFont"]


class TKFont(Font):
    """フォントを設定するオブジェクト"""

    def __init__(
        self,
        family="Meiryo",
        size=14,
        weight="normal",
        slant="roman",
        underline=False,
        overstrike=False,
        font=None,
        root=None,
    ):
        rootj = False
        if not isinstance(root, Misc):
            root = Tk()
            rootj = True
        if isinstance(font, Getfont):
            super().__init__(root, font=(font.family[0], int(font.size)))
        elif isinstance(font, Font):
            super().__init__(
                font=font,
                root=root,
            )
        else:
            fontlist = families(root)
            family = family if family in fontlist else fontlist[0]
            if isinstance(size, int | float):
                size = size
            else:
                size = 14
            weight = listchose(weight, ["normal", "bold"])
            slant = listchose(slant, ["roman", "italic"])
            underline = bols(underline, False)
            overstrike = bols(overstrike, False)
            super().__init__(
                root,
                family=family,
                size=size,
                weight=weight,
                slant=slant,
                underline=underline,
                overstrike=overstrike,
            )
        if rootj:
            root.destroy()
