from tkinter import Misc, Tk
from tkinter.font import Font, families

from ...dev import bols, listchose, nums

__all__ = ["fonts"]


class fonts(Font):
    def __init__(
        self,
        family="Meiryo",
        size=14,
        weight="normal",
        slant="roman",
        underline=False,
        overstrike=False,
        root=None,
    ):
        self.rootj = False
        self.root = root
        if not isinstance(self.root, Misc):
            self.root = (Tk(),)
            self.rootj = True
        self.fontlist = families(self.root)
        self.family = family if family in self.fontlist else self.fontlist[0]
        if self.rootj:
            self.root.destroy()
        self.size = nums(size, 14)
        self.weight = listchose(weight, ["normal", "bold"])
        self.slant = listchose(slant, ["roman", "italic"])
        self.underline = bols(underline, False)
        self.overstrike = bols(overstrike, False)
        super().__init__(
            family=self.family,
            size=self.size,
            weight=self.weight,
            slant=self.slant,
            underline=self.underline,
            overstrike=self.overstrike,
            root=self.root,
        )
