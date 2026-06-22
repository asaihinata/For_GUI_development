from typing import ClassVar

from ..maindialog import _Dialog

__all__ = ["_Dialog", "asksaveasfilename"]


class SaveAs(_Dialog):
    command: ClassVar[str] = "tk_getSaveFile"


def asksaveasfilename(**options):
    return SaveAs(**options).show()
