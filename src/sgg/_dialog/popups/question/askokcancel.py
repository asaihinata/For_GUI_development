from ...maindialog import _iconset, _show

__all__ = ["popupokcansel"]


def askokcancel(title=None, message=None, **kw):
    return _show(title, message, "question", "okcancel", **kw) == "ok"


class popupoc:
    def get_select(self):
        return self.retul

    def __bool__(self):
        return bool(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Question")
        self.message = kw.get("message", "Question message")
        self.icon = _iconset(kw.get("icon"), "question")
        self.retul = askokcancel(title=self.title, message=self.message, icon=self.icon)


def popupokcansel(title="Question", message="Question message", icon="question"):
    return popupoc(title=title, message=message, icon=icon).get_select()
