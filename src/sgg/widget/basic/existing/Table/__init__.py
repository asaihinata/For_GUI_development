from tkinter.ttk import Style, Treeview

import numpy as np

from sgg.dev import num0s, parsecolor
from sgg.widget.base import TElement

__all__ = ["Table"]


class Table(TElement):
    def __init__(self, master, kw):
        def _func(v):
            return v if 2 <= v.ndim else _func(v[np.newaxis, :])

        super().__init__(master, kw)
        values = kw.get("values")
        if not isinstance(values, list | tuple | range | np.ndarray):
            raise TypeError
        self.values = _func(np.array(values)).tolist()
        header = kw.get("header", [])
        if not isinstance(header, list | tuple | range | np.ndarray):
            raise TypeError
        self.header = np.array(header, ndmin=1, ndmax=1).tolist()
        self.header_fg = parsecolor(kw.get("header_fg"), "#000000")
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.header_bg = parsecolor(kw.get("header_bg"), "#cccccc")
        self.colwidth = num0s(kw.get("colwidth"), 120)
        self.height = num0s(kw.get("height"), max(len(self.values), 1))
        self.rowheight = num0s(kw.get("rowheight"), 50)
        self.rowheader = kw.get("rowheader", [])
        self.stylename = f"Table{kw.get("count")}.Treeview"
        self.styleheadingname = f"{self.stylename}.Heading"
        self.style_list = [self.stylename, self.styleheadingname]
        self._widget = Treeview(
            self.master,
            show="headings",
            style=self.stylename,
            height=self.height,
            takefocus=self.takefocus,
        )
        self.style = Style()
        self.style.configure(
            style=self.styleheadingname,
            background=self.header_bg,
            foreground=self.header_fg,
            font=self.font,
        )
        self._widget.configure(style=self.styleheadingname)
        self.style.configure(
            style=self.stylename,
            background=self.bg,
            foreground=self.fg,
            fieldbackground=self.bg,
            font=self.font,
            rowheight=self.rowheight,
        )
        self._widget.configure(style=self.stylename)
        columns = []
        if self.rowheader:
            columns.append("rowheader")
        if self.header:
            columns += self.header
        else:
            if 0 < len(self.values):
                columns += [f"col_{str(i)}" for i in range(len(self.values[0]))]
        self._widget["columns"] = columns
        rows = " " if self.rowheader else "行"
        for col in columns:
            self._widget.heading(
                col, text=rows if col == "rowheader" else col if self.header else ""
            )
            self._widget.column(col, anchor="center", width=self.colwidth)
        self._widget.tag_configure(
            "rowheader_tag", background=self.header_bg, foreground=self.header_fg
        )
        if self.rowheader:
            for i, row in enumerate(self.values):
                self._widget.item(
                    self._widget.insert(
                        "",
                        "end",
                        values=[self.rowheader[i] if i < len(self.rowheader) else ""]
                        + row,
                    ),
                    tags=("rowheader_tag"),
                )
        else:
            for row in self.values:
                self._widget.insert("", "end", values=row)
        self._widget.grid_rowconfigure(0, weight=1)
        self._widget.grid_columnconfigure(0, weight=1)

    def clear_width(self, total_width=None):
        columns = self._widget["columns"]
        if total_width == None:
            self._widget.update_idletasks()
            total_width = self._widget.winfo_width()
        width = int(total_width / len(columns))
        if 0 < len(columns):
            for col in columns:
                self._widget.column(col, width=width)

    def delta(self):
        self._widget.destroy()
