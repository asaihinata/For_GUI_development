from ...maindialog import _iconset, _show

__all__ = ["popupquestion"]


def askquestion(title=None, message=None, **kw):
    return _show(title, message, "question", "yesno", **kw)


class Popupq:
    def __str__(self):
        return str(self.retul)

    def get_select(self):
        return self.retul

    def __init__(self, **kw):
        self.title = kw.get("title", "Question")
        self.message = kw.get("message", "Question message")
        self.icon = _iconset(kw.get("icon"), "question")
        self.retul = askquestion(title=self.title, message=self.message, icon=self.icon)


def popupquestion(title="Question", message="Question message", icon="question"):
    return Popupq(title=title, message=message, icon=icon).get_select()
