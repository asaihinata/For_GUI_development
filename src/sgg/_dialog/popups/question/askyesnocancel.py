from ...maindialog import _iconset, _show

__all__ = ["popupyesnocansel"]


def askyesnocancel(title=None, message=None, **kw):
    s = str(_show(title, message, "question", "yesnocancel", **kw))
    return None if s == "cancel" else s == "yes"


class popupync:
    def get_select(self):
        return self.retul

    def __bool__(self):
        return bool(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Question")
        self.message = kw.get("message", "Question message")
        self.icon = _iconset(kw.get("icon"), "question")
        self.retul = askyesnocancel(
            title=self.title, message=self.message, icon=self.icon
        )


def popupyesnocansel(title="Question", message="Question message", icon="question"):
    return popupync(title=title, message=message, icon=icon).get_select()
