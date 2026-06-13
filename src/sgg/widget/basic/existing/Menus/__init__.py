from tkinter import Menu

from ...common import *

__all__ = ["Menus"]


class Menus(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.menu_lists = kw.get("list", [])
        self.funcs = None
        self.tearoff = bols(kw.get("tearoff"), False)
        self.widget = Menu(
            self.master,
            takefocus=self.takefocus,
            relief=self.relief,
            cursor=self.cursor,
            tearoff=self.tearoff,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            borderwidth=self.borderwidth,
        )
        self._create_menu_lists()

    def _create_menu_lists(self):
        self.widget.delete(0, "end")
        for menus in self.menu_lists:
            if not isinstance(menus, list):
                continue
            for i in range(0, len(menus), 2):
                if len(menus) <= i + 1:
                    break
                submenu = Menu(
                    self.widget,
                    tearoff=self.tearoff,
                    bg=self.bg,
                    fg=self.fg,
                    font=self.font,
                )
                self._add_items_recursive(menu=submenu, items=menus[i + 1])
                self.widget.add_cascade(label=menus[i], menu=submenu)

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
                if self.funcs:
                    menu.add_command(
                        label=item.get("label", ""),
                        command=lambda f=self.funcs: self._exec_funcs(f),
                    )
                else:
                    menu.add_command(label=item.get("label", ""))
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

    def get(self):
        return self.menu_lists

    def clear(self):
        self.widget.delete(0, "end")
        self.menu_lists = []

    def addmenu(self, label, submenu_lists):
        self.menu_lists.append([label, submenu_lists])
        self._create_menu_lists()

    def delta(self):
        self.widget.destroy()

    def set_bg(self, bg):
        self.bg = parsecolor(bg, self.bg)
        self.widget.config(bg=self.bg)

    def get_bg(self):
        return self.bg
