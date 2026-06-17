from ..typing import L, Type_icon

__all__ = ["popup"]

def popup(
    title: str = "Information",
    message: str = "Information message",
    icon: Type_icon = "info",
) -> L["ok"]: ...
