from ...maindialog import _iconset, _show

__all__ = ["popuptrys"]


def askretrycancel(title=None, message=None, **kw):
    return _show(title, message, "warning", "retrycancel", **kw) == "retry"


class popuptry:
    def get_select(self):
        return self.retul

    def __bool__(self):
        return bool(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Question")
        self.message = kw.get("message", "Question message")
        self.icon = _iconset(kw.get("icon"), "question")
        self.retul = askretrycancel(
            title=self.title, message=self.message, icon=self.icon
        )


def popuptrys(title="Question", message="Question message", icon="question"):
    return popuptry(title=title, message=message, icon=icon).get_select()
