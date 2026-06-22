from ...maindialog import _iconset, _show

__all__ = ["popupwarning", "popupwarningyesno"]


def showwarning(title=None, message=None, **kw):
    return _show(title, message, "warning", "ok", **kw)


class Popupw:
    def get_select(self):
        return self.retul

    def __str__(self):
        return str(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Warning")
        self.message = kw.get("message", "Warning message")
        self.icon = _iconset(kw.get("icon"), "warning")
        self.retul = showwarning(title=self.title, message=self.message, icon=self.icon)


class Popupwyn:
    def get_select(self):
        return self.retul

    def __str__(self):
        return str(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Warning")
        self.message = kw.get("message", "Warning message")
        self.icon = _iconset(kw.get("icon"), "warning")
        self.retul = showwarning(
            title=self.title, message=self.message, icon=self.icon, type="yesno"
        )


def popupwarning(title="Warning", message="Warning message", icon="warning"):
    return Popupw(title=title, message=message, icon=icon).get_select()


def popupwarningyesno(title="Warning", message="Warning message", icon="warning"):
    return Popupwyn(title=title, message=message, icon=icon).get_select()
