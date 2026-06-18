from tkinter import Menu, Menubutton

from ...common import *

__all__ = ["Menubuttons"]


class Menubuttons(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.text = kw.get("text")
        self.menu_lists = kw.get("list", [])
        self.tearoff = bols(kw.get("tearoff"), False)
        self.widget = Menubutton(
            self.master,
            takefocus=self.takefocus,
            anchor=self.anchor,
            padx=self.padx,
            pady=self.pady,
            relief=self.relief,
            cursor=self.cursor,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            borderwidth=self.borderwidth,
        )
        self.mainmenu = Menu(
            self.widget, tearoff=self.tearoff, bg=self.bg, fg=self.fg, font=self.font
        )
        self._create_menu_lists()
        self.widget["menu"] = self.mainmenu

    def _create_menu_lists(self):
        for menus in self.menu_lists:
            lens = len(menus)
            if not isinstance(menus, list):
                continue
            for i in range(0, lens, 2):
                if lens <= i + 1:
                    break
                submenu = Menu(
                    self.mainmenu,
                    tearoff=self.tearoff,
                    bg=self.bg,
                    fg=self.fg,
                    font=self.font,
                )
                self._add_items_recursive(menu=submenu, items=menus[i + 1])
                self.mainmenu.add_cascade(label=menus[i], menu=submenu)

    def _add_items_recursive(self, menu: Menu, items):
        i = 0
        while i < len(items):
            item = items[i]
            if item == "---":
                menu.add_separator()
                i += 1
                continue
            if isinstance(item, dict):
                self.funcs = item.get("function")
                menu.add_command(
                    label=item.get("label"),
                    command=lambda f=self.funcs: self._exec_funcs(f),
                )
                self.funcs = None
                i += 1
                continue
            if isinstance(item, str):
                if i + 1 < len(items) and isinstance(items[i + 1], list):
                    new_sub = Menu(
                        menu,
                        tearoff=self.tearoff,
                        bg=self.bg,
                        fg=self.fg,
                        font=self.font,
                    )
                    self._add_items_recursive(new_sub, items[i + 1])
                    menu.add_cascade(label=item, menu=new_sub)
                    i += 2
                    continue
                else:
                    menu.add_command(label=item)
                    i += 1
                    continue
            if isinstance(item, list):
                new_sub = Menu(
                    menu, tearoff=self.tearoff, bg=self.bg, fg=self.fg, font=self.font
                )
                self._add_items_recursive(new_sub, item)
                menu.add_cascade(label="Submenu", menu=new_sub)
                i += 1
                continue

    def get_items(self):
        return self.menu_lists

    def clear(self):
        self.mainmenu.delete(0, "end")
        self.menu_lists = []

    def addmenu(self, label, submenu_lists):
        self.menu_lists.append([label, submenu_lists])
        self._create_menu_lists(self.menu_lists)

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
