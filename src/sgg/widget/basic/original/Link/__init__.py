from pathlib import Path
from tkinter import Label, Variable
from webbrowser import open

from sgg.dev import num0, parsecolor
from sgg.font import Getfont, TKFont
from sgg.widget.basic.dev import linkcheck
from sgg.widget.element import Element

__all__ = ["Link"]


class Link(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.link_url = kw.get("link")
        if not isinstance(self.link_url, str | Path):
            raise ValueError
        font = kw.get("font", None)
        if isinstance(font, Getfont):
            self.font = TKFont(
                self.master,
                font=font,
            )
        else:
            self.family = kw.get("family")
            self.font_size = kw.get("font_size")
            self.weight = kw.get("weight")
            self.slant = kw.get("slant")
            self.underline = kw.get("underline")
            self.overstrike = kw.get("overstrike")
            self.font = TKFont(
                self.master,
                self.family,
                self.font_size,
                self.weight,
                self.slant,
                self.underline,
                self.overstrike,
            )
        self.fg = parsecolor(kw.get("fg"), "#0000ee")
        self.wraplength = num0(kw.get("wraplength"))
        self.textvariable = Variable(value=kw.get("text"))
        self._widget = Label(
            master,
            anchor=self.anchor,
            bg=self.bg,
            borderwidth=self.borderwidth,
            cursor=self.cursor,
            fg=self.fg,
            font=self.font,
            height=self.height,
            justify=self.justify,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            takefocus=self.takefocus,
            textvariable=self.textvariable,
            width=self.width,
            wraplength=self.wraplength,
        )
        self._widget.bind("<Button-1>", self._link)

    def _link(self, ev):
        if isinstance(self.link_url, Path):
            if self.link_url.is_file() and self.link_url.suffix in [".html", ".htm"]:
                open(str(Path(f"file://{self.link_url}").resolve()))
        elif linkcheck(self.link_url):
            open(self.link_url)

    def delta(self):
        self._widget.destroy()

    def get_text(self):
        return self.textvariable.get()

    def set_text(self, txt):
        self.textvariable.set(txt)
        self._widget.config(textvariable=self.textvariable)

    def get_link(self):
        return self.link_url

    def set_link(self, link):
        self.link_url = link
