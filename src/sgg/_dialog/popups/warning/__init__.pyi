from ..typing import L, Type_icon

__all__ = ["popupwarning", "popupwarningyesno"]

def popupwarning(
    title: str = "Warning",
    message: str = "Warning message",
    icon: Type_icon = "warning",
) -> L["ok"]: ...
def popupwarningyesno(
    title: str = "Warning",
    message: str = "Warning message",
    icon: Type_icon = "warning",
) -> L["yes", "no"]: ...
