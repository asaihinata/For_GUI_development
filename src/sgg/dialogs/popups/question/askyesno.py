from ...maindialog import _iconset, _show

__all__ = ["popupyesno"]


def askyesno(title=None, message=None, **kw):
    return _show(title, message, "question", "yesno", **kw) == "yes"


class popupyn:
    def get_select(self):
        return self.retul

    def __bool__(self):
        return bool(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Question")
        self.message = kw.get("message", "Question message")
        self.icon = _iconset(kw.get("icon"), "question")
        self.retul = askyesno(title=self.title, message=self.message, icon=self.icon)


def popupyesno(title="Question", message="Question message", icon="question"):
    return popupyn(title=title, message=message, icon=icon).get_select()
