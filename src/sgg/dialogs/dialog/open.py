from os.path import split
from typing import ClassVar

from ..maindialog import _Dialog

__all__ = ["Open", "askopenfilename"]


class Open(_Dialog):
    command: ClassVar[str] = "tk_getOpenFile"

    def _fixresult(self, widget, result):
        if isinstance(result, tuple):
            result = tuple([getattr(r, "string", r) for r in result])
            if result:
                path, _ = split(result[0])
                self.options["initialdir"] = path
            return result
        if not widget.tk.wantobjects() and "multiple" in self.options:
            return self._fixresult(widget, widget.tk.splitlist(result))
        return _Dialog._fixresult(self, widget, result)


def askopenfilename(**options):
    return Open(**options).show()
