from typing import Literal

from sgg._typing import Type_icon

__all__ = ["popuperror", "popuperroryesno"]

def popuperror(
    title: str = "Error", message: str = "Error message", icon: Type_icon = "error"
) -> Literal["ok"]: ...
def popuperroryesno(
    title: str = "Error", message: str = "Error message", icon: Type_icon = "error"
) -> Literal["yes", "no"]: ...
