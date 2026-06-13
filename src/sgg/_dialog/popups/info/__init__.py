from ...maindialog import _iconset, _show

__all__ = ["popup"]


def showinfo(title=None, message=None, **kw):
    return _show(title, message, "info", "ok", **kw)


class popups:
    def __init__(self, **kw):
        self.title = kw.get("title", "Information")
        self.message = kw.get("message", "Information message")
        self.icon = _iconset(kw.get("icon"), "info")
        self.retul = showinfo(title=self.title, message=self.message, icon=self.icon)

    def get_select(self):
        return self.retul

    def __str__(self):
        return str(self.retul)


def popup(title="Information", message="Information message", icon="info"):
    return popups(title=title, message=message, icon=icon).get_select()
