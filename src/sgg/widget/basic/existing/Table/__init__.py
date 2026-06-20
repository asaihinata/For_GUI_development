from tkinter.ttk import Style, Treeview

from ...common import *

__all__ = ["Table"]


class Table(Element):
    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.header_fg = parsecolor(kw.get("header_fg"), "#000000")
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.header_bg = parsecolor(kw.get("header_bg"), "#cccccc")
        self.values = kw.get("values", [])
        self.header = kw.get("header", [])
        self.colwidth = num0s(kw.get("colwidth"), 120)
        self.height = num0s(kw.get("height"), max(len(self.values), 1))
        self.rowheight = num0s(kw.get("rowheight"), 50)
        self.rowheader = kw.get("rowheader", [])
        self.stylename = f"Table{kw.get('count')}.Treeview"
        self.widget = Treeview(
            self.master,
            show="headings",
            style=self.stylename,
            height=self.height,
            takefocus=self.takefocus,
        )
        style = Style()
        style.configure(
            style=f"{self.stylename}.Heading",
            background=self.header_bg,
            foreground=self.header_fg,
            font=self.font,
        )
        self.widget.configure(style=f"{self.stylename}.Heading")
        style.configure(
            style=self.stylename,
            background=self.bg,
            foreground=self.fg,
            fieldbackground=self.bg,
            font=self.font,
            rowheight=self.rowheight,
        )
        self.widget.configure(style=self.stylename)
        columns = []
        if self.rowheader:
            columns.append("rowheader")
        if self.header:
            columns += self.header
        else:
            if 0 < len(self.values):
                columns += [f"col_{str(i)}" for i in range(len(self.values[0]))]
        self.widget["columns"] = columns
        rows = " " if self.rowheader else "行"
        for col in columns:
            self.widget.heading(
                col, text=rows if col == "rowheader" else col if self.header else ""
            )
            self.widget.column(col, anchor="center", width=self.colwidth)
        self.widget.tag_configure(
            "rowheader_tag", background=self.header_bg, foreground=self.header_fg
        )
        if self.rowheader:
            for i, row in enumerate(self.values):
                self.widget.item(
                    self.widget.insert(
                        "",
                        "end",
                        values=[self.rowheader[i] if i < len(self.rowheader) else ""]
                        + row,
                    ),
                    tags=("rowheader_tag"),
                )
        else:
            for row in self.values:
                self.widget.insert("", "end", values=row)
        self.widget.grid_rowconfigure(0, weight=1)
        self.widget.grid_columnconfigure(0, weight=1)

    def clear_width(self, total_width=None):
        columns = self.widget["columns"]
        if total_width == None:
            self.widget.update_idletasks()
            total_width = self.widget.winfo_width()
        width = int(total_width / len(columns))
        if 0 < len(columns):
            for col in columns:
                self.widget.column(col, width=width)

    def delta(self):
        self.widget.destroy()
