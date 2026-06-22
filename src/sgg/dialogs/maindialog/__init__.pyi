from collections.abc import Mapping
from tkinter import Misc
from typing import Any, ClassVar, Literal

class Dialog:
    command: ClassVar[str | None]
    master: Misc | None
    options: Mapping[str, Any]
    def __init__(self, master: Misc | None = None, **options: Any) -> None: ...
    def show(self, **options: Any) -> Any: ...

class _Dialog(Dialog): ...

class Message(Dialog):
    command: ClassVar[str]

def _show(
    title: str | None = None,
    message: str | None = None,
    _icon: str | None = None,
    _type: str | None = None,
    **kw,
) -> str: ...
def _iconset(
    icon: Literal["info", "error", "warning", "question"] | str,
    other: Literal["info", "error", "warning", "question"] | str = "info",
) -> str: ...
