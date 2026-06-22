from ...maindialog import _iconset, _show

__all__ = ["popuperror", "popuperroryesno"]


def showerror(title=None, message=None, **kw):
    return _show(title, message, "error", "ok", **kw)


class Popupe:
    def get_select(self):
        return self.retul

    def __str__(self):
        return str(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Error")
        self.message = kw.get("message", "Error message")
        self.icon = _iconset(kw.get("icon"), "error")
        self.retul = showerror(title=self.title, message=self.message, icon=self.icon)


class Popupeyn:
    def get_select(self):
        return self.retul

    def __str__(self):
        return str(self.retul)

    def __init__(self, **kw):
        self.title = kw.get("title", "Error")
        self.message = kw.get("message", "Error message")
        self.icon = _iconset(kw.get("icon"), "error")
        self.retul = showerror(
            title=self.title, message=self.message, icon=self.icon, type="yesno"
        )


def popuperror(title="Error", message="Error message", icon="error"):
    return Popupe(title=title, message=message, icon=icon).get_select()


def popuperroryesno(title="Error", message="Error message", icon="error"):
    return Popupeyn(title=title, message=message, icon=icon).get_select()
