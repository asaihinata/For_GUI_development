from pathlib import Path
from tkinter import Label
from webbrowser import open

from sgg.dev import num0, parsecolor
from sgg.font import TKFont
from sgg.widget.base import Element
from sgg.widget.basic.dev import linkcheck

__all__ = ["Link"]


class Link(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.link_url = kw.get("link")
        if not isinstance(self.link_url, str | Path):
            raise ValueError("linkにはstr型もしくはPathオブジェクトを指定してください")
        self.underline = kw.get("underline", True)
        self.font = TKFont(
            master,
            self.family,
            self.font_size,
            self.weight,
            self.slant,
            self.underline,
            self.overstrike,
        )
        self.fg = parsecolor(kw.get("fg"), "#0000ee")
        self.wraplength = num0(kw.get("wraplength"))
        self.text = kw.get("text")
        if self.text == None:
            self.text = self.link_url
        self.widget = Label(
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
            text=self.text,
            width=self.width,
            wraplength=self.wraplength,
        )
        self.widget.bind("<Button-1>", self._link)

    def _link(self, ev):
        if isinstance(self.link_url, Path):
            if self.link_url.is_file() and self.link_url.suffix in [".html", ".htm"]:
                open(str(Path(f"file://{self.link_url}").resolve()))
        elif linkcheck(self.link_url):
            open(self.link_url)

    def delta(self):
        self.widget.destroy()

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.widget.config(text=txt)

    def get_link(self):
        return self.link_url

    def set_link(self, link):
        self.link_url = link
