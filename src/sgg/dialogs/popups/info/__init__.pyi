from typing import Literal

from sgg.typing import Type_icon

__all__ = ["popup"]

def popup(
    title: str = "Information",
    message: str = "Information message",
    icon: Type_icon = "info",
) -> Literal["ok"]: ...
