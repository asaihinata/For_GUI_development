from ..typing import L, Type_icon

__all__ = ["popuperror", "popuperroryesno"]

def popuperror(
    title: str = "Error", message: str = "Error message", icon: Type_icon = "error"
) -> L["ok"]: ...
def popuperroryesno(
    title: str = "Error", message: str = "Error message", icon: Type_icon = "error"
) -> L["yes", "no"]: ...
