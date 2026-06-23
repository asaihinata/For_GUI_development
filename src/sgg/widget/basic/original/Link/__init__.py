from pathlib import Path
from tkinter import Label
from webbrowser import open

from .....font import TKFont
from ...common import *
from ...dev import linkcheck

__all__ = ["Link"]


class Link(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.link_url = kw.get("link")
        if not isinstance(self.link_url, str | Path):
            raise ValueError("linkにはstr型もしくはPathオブジェクトを指定してください")
        self.underline = kw.get("underline", True)
        self.font = TKFont(
            self.family,
            self.font_size,
            self.weight,
            self.slant,
            self.underline,
            self.overstrike,
            root=master,
        )
        self.fg = parsecolor(kw.get("fg"), "#0000ee")
        self.wraplength = num0(kw.get("wraplength"))
        self.text = kw.get("text")
        if self.text == None:
            self.text = self.link_url
        self.widget = Label(
            master,
            takefocus=self.takefocus,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            wraplength=self.wraplength,
            cursor=self.cursor,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            width=self.width,
            height=self.height,
            justify=self.justify,
            borderwidth=self.borderwidth,
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

    def set_fg(self, fg):
        self.fg = parsecolor(fg, self.fg)
        self.widget.config(fg=self.fg)

    def set_bg(self, bg):
        self.bg = parsecolor(bg, self.bg)
        self.widget.config(bg=self.bg)

    def get_fg(self):
        return self.fg

    def get_bg(self):
        return self.bg
