from typing import Literal

from sgg._typing import Type_icon

__all__ = ["popup"]

def popup(
    title: str = "Information",
    message: str = "Information message",
    icon: Type_icon = "info",
) -> Literal["ok"]: ...
