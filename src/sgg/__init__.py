from .dialogs import *
from .graph import *
from .nparray import *
from .readfile import Getcsv, Getfont, Getjosn
from .version import __version__
from .widget import *

__all__ = (
    ["__version__", "Getjosn", "Getcsv", "Getfont", "Guis"]
    + getattr(dialogs, "__all__", [])
    + getattr(graph, "__all__", [])
    + getattr(nparray, "__all__", [])
    + getattr(widget, "__all__", [])
)


def __dir__():
    return __all__ + [k for k in globals() if k.startswith("__") and k.endswith("__")]


def _counts():
    Guis._count += 1
    return Guis._count


class Guis:
    _count = 0

    @classmethod
    def window(cls, **kw):
        return WindowController(kw)

    @staticmethod
    def Menus(**kw):
        return {"count": _counts(), "type": "Menus", **kw}

    @staticmethod
    def Menubuttons(**kw):
        return {"count": _counts(), "type": "Menubuttons", **kw}

    @staticmethod
    def Texts(**kw):
        return {"count": _counts(), "type": "Texts", **kw}

    @staticmethod
    def Link(**kw):
        return {"count": _counts(), "type": "Link", **kw}

    @staticmethod
    def Images(**kw):
        return {"count": _counts(), "type": "Images", **kw}

    @staticmethod
    def Imagebyte(**kw):
        return {"count": _counts(), "type": "Imagebyte", **kw}

    @staticmethod
    def Imagelink(**kw):
        return {"count": _counts(), "type": "Imagelink", **kw}

    @staticmethod
    def Buttons(**kw):
        return {"count": _counts(), "type": "Buttons", **kw}

    @staticmethod
    def Input(**kw):
        return {"count": _counts(), "type": "Input", **kw}

    @staticmethod
    def Multiline(**kw):
        return {"count": _counts(), "type": "Multiline", **kw}

    @staticmethod
    def Table(**kw):
        return {"count": _counts(), "type": "Table", **kw}

    @staticmethod
    def Tree(**kw):
        return {"count": _counts(), "type": "Tree", **kw}

    @staticmethod
    def Listboxs(**kw):
        return {"count": _counts(), "type": "Listboxs", **kw}

    @staticmethod
    def TCombobox(**kw):
        return {"count": _counts(), "type": "TCombobox", **kw}

    @staticmethod
    def Radio(**kw):
        return {"count": _counts(), "type": "Radio", **kw}

    @staticmethod
    def Checkbox(**kw):
        return {"count": _counts(), "type": "Checkbox", **kw}

    @staticmethod
    def Frames(**kw):
        return {"count": _counts(), "type": "Frames", **kw}

    @staticmethod
    def Column(**kw):
        return {"count": _counts(), "type": "Column", **kw}

    @staticmethod
    def Slidebar(**kw):
        return {"count": _counts(), "type": "Slidebar", **kw}

    @staticmethod
    def InputNumber(**kw):
        return {"count": _counts(), "type": "InputNumber", **kw}

    @staticmethod
    def FileLoad(**kw):
        return {"count": _counts(), "type": "FileLoad", **kw}

    @staticmethod
    def FolderLoad(**kw):
        return {"count": _counts(), "type": "FolderLoad", **kw}

    @staticmethod
    def Colorbtn(**kw):
        return {"count": _counts(), "type": "Colorbtn", **kw}

    @staticmethod
    def Savebtn(**kw):
        return {"count": _counts(), "type": "Savebtn", **kw}

    @staticmethod
    def Tab(**kw):
        return {"count": _counts(), "type": "Tab", **kw}

    @staticmethod
    def TProgressbar(**kw):
        return {"count": _counts(), "type": "TProgressbar", **kw}

    @staticmethod
    def Barcode(**kw):
        return {"count": _counts(), "type": "Barcode", **kw}

    @staticmethod
    def QRImage(**kw):
        return {"count": _counts(), "type": "QRImage", **kw}

    @staticmethod
    def LineGraph(**kw):
        return {"count": _counts(), "type": "LineGraph", **kw}

    @staticmethod
    def BarGraph(**kw):
        return {"count": _counts(), "type": "BarGraph", **kw}

    @staticmethod
    def BarhGraph(**kw):
        return {"count": _counts(), "type": "BarhGraph", **kw}

    @staticmethod
    def Funne(**kw):
        return {"count": _counts(), "type": "Funne", **kw}

    @staticmethod
    def Pie(**kw):
        return {"count": _counts(), "type": "Pie", **kw}

    @staticmethod
    def Boxplot(**kw):
        return {"count": _counts(), "type": "Boxplot", **kw}

    @staticmethod
    def Waterfall(**kw):
        return {"count": _counts(), "type": "Waterfall", **kw}

    @staticmethod
    def Waterfallh(**kw):
        return {"count": _counts(), "type": "Waterfallh", **kw}

    @staticmethod
    def Scatter(**kw):
        return {"count": _counts(), "type": "Scatter", **kw}

    @staticmethod
    def DScatter(**kw):
        return {"count": _counts(), "type": "DScatter", **kw}

    @staticmethod
    def Stem(**kw):
        return {"count": _counts(), "type": "Stem", **kw}

    @staticmethod
    def Step(**kw):
        return {"count": _counts(), "type": "Step", **kw}

    @staticmethod
    def Stack(**kw):
        return {"count": _counts(), "type": "Stack", **kw}

    @staticmethod
    def Hist(**kw):
        return {"count": _counts(), "type": "Hist", **kw}

    @staticmethod
    def Linefill(**kw):
        return {"count": _counts(), "type": "Linefill", **kw}

    @staticmethod
    def Ecdf(**kw):
        return {"count": _counts(), "type": "Ecdf", **kw}

    @staticmethod
    def Errorbar(**kw):
        return {"count": _counts(), "type": "Errorbar", **kw}

    @staticmethod
    def Eventplot(**kw):
        return {"count": _counts(), "type": "Eventplot", **kw}

    @staticmethod
    def Hatplot(**kw):
        return {"count": _counts(), "type": "Hatplot", **kw}

    @staticmethod
    def Hist2d(**kw):
        return {"count": _counts(), "type": "Hist2d", **kw}

    @staticmethod
    def Violinplot(**kw):
        return {"count": _counts(), "type": "Violinplot", **kw}

    @staticmethod
    def Hexbin(**kw):
        return {"count": _counts(), "type": "Hexbin", **kw}

    @staticmethod
    def Stacked(**kw):
        return {"count": _counts(), "type": "Stacked", **kw}

    @staticmethod
    def Stackedh(**kw):
        return {"count": _counts(), "type": "Stackedh", **kw}

    @staticmethod
    def Barpolar(**kw):
        return {"count": _counts(), "type": "Barpolar", **kw}

    @staticmethod
    def Stempolar(**kw):
        return {"count": _counts(), "type": "Stempolar", **kw}

    @staticmethod
    def Errorpolar(**kw):
        return {"count": _counts(), "type": "Errorpolar", **kw}

    @staticmethod
    def Linepolar(**kw):
        return {"count": _counts(), "type": "Linepolar", **kw}

    @staticmethod
    def Eventpolar(**kw):
        return {"count": _counts(), "type": "Eventpolar", **kw}

    @staticmethod
    def Scatterpolar(**kw):
        return {"count": _counts(), "type": "Scatterpolar", **kw}

    @staticmethod
    def RadarLine(**kw):
        return {"count": _counts(), "type": "RadarLine", **kw}

    @staticmethod
    def RadarFill(**kw):
        return {"count": _counts(), "type": "RadarFill", **kw}

    @classmethod
    def Popup(cls, **kw):
        return popup(**kw)

    @classmethod
    def Popupwarning(cls, **kw):
        return popupwarning(**kw)

    @classmethod
    def Popupwarningyesno(cls, **kw):
        return popupwarningyesno(**kw)

    @classmethod
    def Popuperror(cls, **kw):
        return popuperror(**kw)

    @classmethod
    def Popuperroryesno(cls, **kw):
        return popuperroryesno(**kw)

    @classmethod
    def Popupquestion(cls, **kw):
        return popupquestion(**kw)

    @classmethod
    def Popupokcancel(cls, **kw):
        return popupokcansel(**kw)

    @classmethod
    def Popupyesno(cls, **kw):
        return popupyesno(**kw)

    @classmethod
    def Popupyesnocancel(cls, **kw):
        return popupyesnocansel(**kw)

    @classmethod
    def Popuptry(cls, **kw):
        return popuptrys(**kw)
