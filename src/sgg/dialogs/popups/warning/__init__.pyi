from ..typing import Literal, Type_icon

__all__ = ["popupwarning", "popupwarningyesno"]

def popupwarning(
    title: str = "Warning",
    message: str = "Warning message",
    icon: Type_icon = "warning",
) -> Literal["ok"]: ...
def popupwarningyesno(
    title: str = "Warning",
    message: str = "Warning message",
    icon: Type_icon = "warning",
) -> Literal["yes", "no"]: ...
