from ..typing import L, Type_icon

__all__ = [
    "popupokcansel",
    "popupquestion",
    "popuptrys",
    "popupyesno",
    "popupyesnocansel",
]

def popupokcansel(
    title: str = "Question",
    message: str = "Question message",
    icon: Type_icon = "question",
) -> bool: ...
def popupquestion(
    title: str = "Question",
    message: str = "Question message",
    icon: Type_icon = "question",
) -> L["yes", "no"]: ...
def popuptrys(
    title: str = "Question",
    message: str = "Question message",
    icon: Type_icon = "question",
) -> bool: ...
def popupyesno(
    title: str = "Question",
    message: str = "Question message",
    icon: Type_icon = "question",
) -> bool: ...
def popupyesnocansel(
    title: str = "Question",
    message: str = "Question message",
    icon: Type_icon = "question",
) -> bool | None: ...
