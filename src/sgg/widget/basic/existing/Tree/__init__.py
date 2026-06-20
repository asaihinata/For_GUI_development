from tkinter.ttk import Style, Treeview

from ...common import *

__all__ = ["Tree"]


class Tree(Element):
    sums = 1

    def __init__(self, master, kw):
        super().__init__(master, kw)
        self.colwidth = num0s(kw.get("colwidth"), 120)
        self.bg = parsecolor(kw.get("bg"), "#e0e0e0")
        self.header_fg = parsecolor(kw.get("header_fg"), "#000000")
        self.header_bg = parsecolor(kw.get("header_bg"), "#cccccc")
        self.rowheight = num0s(kw.get("rowheight"), 50)
        values = kw.get("values", [])
        if not isinstance(values, list):
            raise TypeError("valuesにlist型を指定してください")
        self.values = values
        header = kw.get("header", [])
        if not isinstance(header, list):
            raise TypeError("headerにlist型を指定してください")
        self.header = header
        self.maxcols = (
            1
            if self._calc_max_columns(self.values) < 1
            else self._calc_max_columns(self.values)
        )
        cols = [f"col{i}" for i in range(1, self.maxcols + 1)]
        self.widget = Treeview(
            self.master,
            columns=cols,
            show="tree" if self.header == [] else "tree headings",
        )
        if self.header != [] and len(self.header) < self.maxcols:
            for i in range(self.maxcols - len(self.header)):
                self.header.append("")
        self.widget.heading("#0", text=kw.get("side_header"))
        self.widget.column("#0", width=200, anchor="w")
        for i, c in enumerate(cols):
            self.widget.heading(c, text="" if self.header == [] else self.header[i])
            self.widget.column(c, width=self.colwidth, anchor="w")
        style = Style()
        self.stylename = f"Tree{kw.get('count')}.Treeview"
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
        self.widget.grid_rowconfigure(0, weight=1)
        self.widget.grid_columnconfigure(0, weight=1)
        self._build_from_values(self.values)
        self.widget.config(height=min(num0(self.sums, 1), 15))

    def _calc_max_columns(self, vals):
        maxc, i, L = 0, 0, len(vals)
        while i < L:
            v = vals[i]
            if isinstance(v, str) and i + 1 < L and isinstance(vals[i + 1], list):
                c = self._maxlen_in_list(vals[i + 1])
                if maxc < c:
                    maxc = c
                i += 2
            else:
                i += 1
        return maxc

    def _maxlen_in_list(self, lst):
        maxc, strings = 0, [x for x in lst if not isinstance(x, list)]
        if maxc < len(strings):
            maxc = len(strings)
        for x in lst:
            if isinstance(x, list):
                c = self._maxlen_in_list(x)
                if maxc < c:
                    maxc = c
        return maxc

    def _flatten_strings(self, lst):
        out = []
        for x in lst:
            if isinstance(x, list):
                out.extend(self._flatten_strings(x))
            else:
                out.append(x)
        return out

    def _build_from_values(self, vals):
        i, L = 0, len(vals)
        while i < L:
            item = vals[i]
            if isinstance(item, str) and i + 1 < L and isinstance(vals[i + 1], list):
                self._process_data_list(
                    self.widget.insert(
                        "", "end", text=item, values=("") * self.maxcols
                    ),
                    item,
                    vals[i + 1],
                )
                self.sums += 2
                i += 2
            else:
                self.sums += 1
                i += 1

    def _process_data_list(self, parent_id, parent_text, data_list):
        summary_values = [x for x in data_list if not isinstance(x, list)]
        summary_id = self.widget.insert(
            parent_id,
            "end",
            text=parent_text,
            values=(
                tuple((str(x) for x in summary_values[: self.maxcols]))
                + tuple("" for _ in range(max(0, self.maxcols - len(summary_values))))
            ),
        )
        for idx, x in enumerate(data_list):
            if isinstance(x, list):
                k, dk = idx - 1, data_list[k]
                while k <= 0 and isinstance(dk, list):
                    k -= 1
                label = dk if 0 <= k and isinstance(dk, str) else ""
                if any(isinstance(s, list) for s in x):
                    nesumval = [s for s in x if not isinstance(s, list)]
                    for y in x:
                        if isinstance(y, list):
                            self._process_data_list(
                                self.widget.insert(
                                    summary_id,
                                    "end",
                                    text=label,
                                    values=tuple(
                                        (str(s) for s in nesumval[: self.maxcols])
                                    )
                                    + tuple(
                                        ""
                                        for _ in range(
                                            max(0, self.maxcols - len(nesumval))
                                        )
                                    ),
                                ),
                                label,
                                y,
                            )
                else:
                    self.widget.insert(
                        summary_id,
                        "end",
                        text=label,
                        values=tuple((str(s) for s in x[: self.maxcols]))
                        + tuple("" for _ in range(max(0, self.maxcols - len(x)))),
                    )

    def _get_iid(self, item=None):
        for child in self.widget.get_children(item):
            yield child
            yield from self._get_iid(child)

    def get_iid(self):
        return list(self._get_iid())

    def expand(self, iid):
        self.widget.item(iid, open=True)

    def collapse(self, iid):
        self.widget.item(iid, open=False)

    def get_path(self, iid):
        parts, cur = [], iid
        while cur:
            txt = self.widget.item(cur, "text")
            if txt:
                parts.append(txt)
            cur = self.widget.parent(cur)
        parts.reverse()
        return "/".join(parts)

    def add_node(self, parent_iid, text, data_list=None):
        pid = self.widget.insert(
            parent_iid, "end", text=text, values=("") * self.maxcols
        )
        if isinstance(data_list, list):
            self._process_data_list(pid, text, data_list)
        return pid

    def delete_node(self, iid):
        self.widget.delete(iid)

    def clear_width(self):
        columns = self.widget["columns"]
        self.widget.update_idletasks()
        if 0 < len(columns):
            for col in columns:
                self.widget.column(
                    col, width=int(self.widget.winfo_width() / len(columns))
                )

    def delta(self):
        self.widget.destroy()
