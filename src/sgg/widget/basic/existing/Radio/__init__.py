from tkinter import Radiobutton, StringVar

from sgg.dev import num0, parsecolor
from sgg.widget.base import Element

__all__ = ["Radio"]


class Radio(Element):
    groups, text_list, count = {}, {}, 0

    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.count += 1
        self.text = kw.get("text")
        self.group = kw.get("group", "default")
        self._count(self.text)
        self.wraplength = num0(kw.get("wraplength", 0))
        self.value = f"{self.text}{self.text_list.get(self.text)}"
        if self.groups.get(self.group) == None:
            self.groups[self.group] = {
                "var": StringVar(),
                "has_default": False,
                "text": self.text,
            }
        group_data = self.groups[self.group]
        self.variable = group_data["var"]
        self.selectcolor = parsecolor(kw.get("selectcolor", "white"), "white")
        self.activebg = parsecolor(kw.get("activebg"))
        self.activefg = parsecolor(kw.get("activefg"))
        self.widget = Radiobutton(
            self.master,
            activebackground=self.activebg,
            activeforeground=self.activefg,
            anchor=self.anchor,
            bg=self.bg,
            borderwidth=self.borderwidth,
            cursor=self.cursor,
            fg=self.fg,
            font=self.font,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            selectcolor=self.selectcolor,
            takefocus=self.takefocus,
            text=self.text,
            value=self.value,
            variable=self.variable,
            wraplength=self.wraplength,
        )
        if not group_data["has_default"]:
            self.variable.set(self.value)
            group_data["has_default"] = True

    def _count(self, val):
        self.text_list[val] = (
            1 if self.text_list.get(val) == None else self.text_list[val] + 1
        )

    def delta(self):
        self.widget.destroy()

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt
        self.widget.config(text=txt)

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
