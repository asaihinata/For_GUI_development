from os import getcwd
from re import findall
from tkinter import Canvas, Frame, Scrollbar, Tk
from types import FunctionType

from PIL import ImageGrab

from ...dev import bols, is_array_like, listchose, num0s, parsecolor, range_num
from ...dialogs import asksaveasfilename
from ...graph import *
from ..basic import *

__all__ = ["WindowController"]


class WindowController:
    """ウィンドウを生成する"""

    count = 0

    def __init__(self, kw):
        self.title = kw.get("title", "window")
        self.layout = kw.get("layout", [])
        if self.layout == None or not isinstance(self.layout, list | tuple):
            raise TypeError("layoutに配列の型を指定してください")
        self.bg = parsecolor(kw.get("bg"), "#64778d")
        self.scroll = bols(kw.get("scroll"), False)
        self.scroll_x = bols(kw.get("scroll_x"), self.scroll)
        self.scroll_y = bols(kw.get("scroll_y"), self.scroll)
        self.root = Tk()
        parent = self.root
        self.root.title(self.title)
        self.root.protocol("WM_DELETE_WINDOW", self._on_window_close)
        self.root.tk_setPalette(background=self.bg)
        self.size = kw.get("size", (None, None))
        self.maxmine = bols(kw.get("maxmine"), False)
        if self.maxmine:
            self.maxwin()
        self.alpha = range_num(num0s(kw.get("alpha"), 1), 0, 1, 1)
        self.fullscreens = bols(kw.get("fullscreen"), False)
        self.topmost = bols(kw.get("topmost"), False)
        self.set_alpha(self.alpha)
        self.fullscreen(self.fullscreens)
        self.foreground(self.topmost)
        resizable = bols(kw.get("resizable"), None)
        if resizable:
            self.resizableswidth, self.resizablesheight = True, True
        else:
            self.resizableswidth = bols(kw.get("resizableswidth"), True)
            self.resizablesheight = bols(kw.get("resizablesheight"), True)
        self.resizable(self.resizableswidth, self.resizablesheight)
        self.location = kw.get("location", (0, 0))
        self.widgets = {}
        self.closed = False
        self._close_result, self.canvas = None, None
        if self.scroll_y or self.scroll_x:
            self.canvas = Canvas(self.root, bg=self.bg, highlightthickness=0)
            self._inner_frame = Frame(self.canvas, bg=self.bg)
            self.canvas.create_window((0, 0), window=self._inner_frame, anchor="nw")
            self._inner_frame.bind(
                "<Configure>",
                lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
            )
            if self.scroll_y:
                ybar = Scrollbar(
                    self.root, orient="vertical", command=self.canvas.yview
                )
                self.canvas.configure(yscrollcommand=ybar.set)
                ybar.pack(side="right", fill="y")
            if self.scroll_x:
                xbar = Scrollbar(
                    self.root, orient="horizontal", command=self.canvas.xview
                )
                self.canvas.configure(xscrollcommand=xbar.set)
                xbar.pack(side="bottom", fill="x")
            self.canvas.pack(fill="both", expand=True)
            parent = self._inner_frame
        if self.size == (None, None):
            x, y = self.location
            try:
                self.root.geometry(f"+{int(x)}+{int(y)}")
            except:
                pass
        else:
            w, h = self.size
            x, y = self.location
            try:
                self.root.geometry(f"{int(w)}x{int(h)}+{int(x)}+{int(y)}")
            except:
                self.root.geometry(f"+{int(x)}+{int(y)}")
        if self.layout:
            self._build_layout(self.layout, parent)
        self.loadfun = kw.get("load")

    def scroll_to(self, key):
        w, y = self.widgets.get(key), 0
        if not self.canvas or not w:
            return
        self.root.update_idletasks()
        try:
            y = self.canvas.canvasy(w.winfo_rooty() - self.canvas.winfo_rooty())
        except:
            return None
        scroll_region = self.canvas.bbox("all")
        if not scroll_region:
            return None
        total_height = scroll_region[3] - scroll_region[1]
        if total_height <= 0:
            return None
        self.canvas.yview_moveto(y / total_height)

    def _build_layout(self, layout, parent, bgcolor=None):
        bg = self.bg if bgcolor == None else bgcolor
        for row in layout:
            row_frame = Frame(parent, bg=bg)
            row_frame.pack(fill="x", padx=5, pady=5)
            for kw in row:
                self._create_element(kw, row_frame, bg)

    def _create_element(self, kw, parent, bgs=None):
        t = kw.get("type")
        key = kw.get("key")
        widget = None
        kw["back_bg"] = bgs
        if key == None:
            kw["key"] = f"widget{self.count}"
        if t == "Menus":
            widget = Menus(parent, kw)
        elif t == "Menubuttons":
            widget = Menubuttons(parent, kw)
        elif t == "Texts":
            widget = Texts(parent, kw)
        elif t == "Link":
            widget = Link(parent, kw)
        elif t == "Images":
            widget = Images(parent, kw)
        elif t == "Imagebyte":
            widget = Imagebyte(parent, kw)
        elif t == "Imagelink":
            widget = Imagelink(parent, kw)
        elif t == "Buttons":
            widget = Buttons(parent, kw)
        elif t == "Input":
            widget = Input(parent, kw)
        elif t == "Multiline":
            widget = Multiline(parent, kw)
        elif t == "Listboxs":
            widget = Listboxs(parent, kw)
        elif t == "TCombobox":
            widget = TCombobox(parent, kw)
        elif t == "InputNumber":
            widget = InputNumber(parent, kw)
        elif t == "Radio":
            widget = Radio(parent, kw)
        elif t == "Checkbox":
            widget = Checkbox(parent, kw)
        elif t == "FileLoad":
            widget = FileLoad(parent, kw)
        elif t == "FolderLoad":
            widget = FolderLoad(parent, kw)
        elif t == "Colorbtn":
            widget = Colorbtn(parent, kw)
        elif t == "Savebtn":
            widget = Savebtn(parent, kw)
        elif t == "TProgressbar":
            widget = TProgressbar(parent, kw)
        elif t == "Tab":
            widget = Tab(parent, kw)
            for tab in kw.get("tabs", []):
                if not isinstance(tab, list | tuple) or len(tab) == 0:
                    continue
                frame = Frame(widget.widget, bg=widget.bg)
                widget._add_tab(frame, tab[0])
                if 1 < len(tab) and isinstance(tab[1], list):
                    self._build_layout(tab[1], frame, kw.get("bg"))
        elif t == "Frames":
            widget = Frames(parent, kw)
            if kw.get("layout"):
                self._build_layout(kw.get("layout"), widget.widget, kw.get("bg"))
        elif t == "Column":
            widget = Column(parent, kw)
            if kw.get("layout"):
                self._build_layout(kw.get("layout"), widget.widget, kw.get("bg"))
        elif t == "Table":
            widget = Table(parent, kw)
        elif t == "Tree":
            widget = Tree(parent, kw)
        elif t == "Slidebar":
            widget = Slidebar(parent, kw)
        elif t == "Barcode":
            widget = Barcode(parent, kw)
        elif t == "QRImage":
            widget = QRImage(parent, kw)
        elif t == "LineGraph":
            widget = LineGraph(parent, kw)
        elif t == "BarGraph":
            widget = BarGraph(parent, kw)
        elif t == "BarhGraph":
            widget = BarhGraph(parent, kw)
        elif t == "Funne":
            widget = Funne(parent, kw)
        elif t == "Stacked":
            widget = Stacked(parent, kw)
        elif t == "Stackedh":
            widget = Stackedh(parent, kw)
        elif t == "Scatter":
            widget = Scatter(parent, kw)
        elif t == "DScatter":
            widget = DScatter(parent, kw)
        elif t == "Pie":
            widget = Pie(parent, kw)
        elif t == "Boxplot":
            widget = Boxplot(parent, kw)
        elif t == "Waterfall":
            widget = Waterfall(parent, kw)
        elif t == "Waterfallh":
            widget = Waterfallh(parent, kw)
        elif t == "Stem":
            widget = Stem(parent, kw)
        elif t == "Step":
            widget = Step(parent, kw)
        elif t == "Stack":
            widget = Stack(parent, kw)
        elif t == "Hist":
            widget = Hist(parent, kw)
        elif t == "Hatplot":
            widget = Hatplot(parent, kw)
        elif t == "Hist2d":
            widget = Hist2d(parent, kw)
        elif t == "Linefill":
            widget = Linefill(parent, kw)
        elif t == "Ecdf":
            widget = Ecdf(parent, kw)
        elif t == "Errorbar":
            widget = Errorbar(parent, kw)
        elif t == "Eventplot":
            widget = Eventplot(parent, kw)
        elif t == "Violinplot":
            widget = Violinplot(parent, kw)
        elif t == "Hexbin":
            widget = Hexbin(parent, kw)
        elif t == "Barpolar":
            widget = Barpolar(parent, kw)
        elif t == "Stempolar":
            widget = Stempolar(parent, kw)
        elif t == "Errorpolar":
            widget = Errorpolar(parent, kw)
        elif t == "Linepolar":
            widget = Linepolar(parent, kw)
        elif t == "Eventpolar":
            widget = Eventpolar(parent, kw)
        elif t == "Scatterpolar":
            widget = Scatterpolar(parent, kw)
        elif t == "RadarLine":
            widget = RadarLine(parent, kw)
        elif t == "RadarFill":
            widget = RadarFill(parent, kw)
        else:
            widget = Texts(parent, {"text": f"Unknown element:{t}"})
        if widget:
            if t == "Menus":
                self.root.config(menu=widget.widget)
            elif widget.graph == True:
                widget._pack()
            else:
                try:
                    widget.widget.pack(side="left", padx=5, pady=5)
                except Exception:
                    widget = Texts(parent, {"text": f"widget error:{t}"}).widget.pack(
                        side="left", padx=5, pady=5
                    )
            if key:
                self.widgets[key] = widget
            else:
                self.widgets[f"widget{self.count}"] = widget
        self.count += 1

    def get(self, key):
        return self.widgets.get(key)

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title
        self.root.title(title)

    def widgetcount(self):
        return self.count

    def widgetdict(self):
        return self.widgets

    def widgetlist(self):
        return list(self.widgets.keys())

    def widgetall(self):
        return list(self.widgets.values())

    def winclose(self):
        return "winclose"

    def _on_window_close(self):
        self._close_result = "winclose"
        self.closed = True
        self.root.destroy()

    def close(self):
        self.root.quit()

    def maxwin(self):
        try:
            self.root.state("zoomed")
        except:
            pass

    def minwin(self):
        try:
            self.root.iconify()
        except:
            pass

    def run(self):
        if self.loadfun:
            self.win_exec_funcs(funcs=self.loadfun)
        if self.canvas:
            self.root.after(100, self._update_region)
        self.root.mainloop()

    def _update_region(self):
        try:
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        except:
            pass

    def win_exec_funcs(self, funcs=None):
        if isinstance(funcs, FunctionType):
            funcs()
        elif isinstance(funcs, list):
            for f in funcs:
                if isinstance(f, FunctionType):
                    f()
                else:
                    raise TypeError("関数ではありません")
        else:
            raise TypeError("関数ではありません")

    def foreground(self, bools=False):
        self.root.attributes("-topmost", bools)

    def fullscreen(self, bools=False):
        self.root.attributes("-fullscreen", bools)

    def set_alpha(self, alpha=1.0):
        self.alpha = alpha
        self.root.attributes("-alpha", self.alpha)

    def get_alpha(self):
        return self.alpha

    def deiconify(self):
        self.root.deiconify()

    def withdraw(self):
        self.root.withdraw()

    def geometry(self):
        return [float(i) for i in findall(r"\d+", self.root.winfo_geometry())]

    def tookphoto(self, file="window", ex=".png"):
        root = self.root
        winx, winy = root.winfo_rootx(), root.winfo_rooty()
        bbox = (winx, winy, winx + root.winfo_width(), winy + root.winfo_height())
        paths = asksaveasfilename(
            title="画像を保存する",
            defaultextension=listchose(
                ex,
                [
                    ".png",
                    ".eps",
                    ".jpg",
                    ".jpeg",
                    ".pdf",
                    ".pgf",
                    ".ps",
                    ".raw",
                    ".rgba",
                    ".svg",
                    ".svgz",
                    ".tif",
                    ".tiff",
                    ".webp",
                ],
            ),
            initialfile=file,
            initialdir=getcwd(),
        )
        ImageGrab.grab(bbox=bbox).save(paths)

    def winsize(self):
        root = self.root
        return root.winfo_width(), root.winfo_height()

    def winwidth(self):
        return self.root.winfo_width()

    def winheight(self):
        return self.root.winfo_height()

    def winxy(self):
        root = self.root
        return root.winfo_x(), root.winfo_y()

    def winx(self):
        return self.root.winfo_x()

    def winy(self):
        return self.root.winfo_y()

    def resizable(self, width=None, height=None):
        if (
            height == None
            and is_array_like(width)
            and len(width) == 2
            and all(isinstance(i, bool) for i in width)
        ):
            width, height = width
        else:
            if width is None or not isinstance(width, bool):
                width = None
            if height is None or not isinstance(height, bool):
                height = None
        self.root.resizable(width=width, height=height)
