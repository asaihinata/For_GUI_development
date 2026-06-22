from collections.abc import Iterable
from tkinter import Misc, StringVar

from _typeshed import StrOrBytesPath

__all__ = ["askcolor", "asksaveasfilename", "askopenfilename", "askdirectory"]

def askcolor(
    color: str | bytes | None = None,
    *,
    initialcolor: str = ...,
    parent: Misc = ...,
    title: str = ...,
) -> tuple[None, None] | tuple[tuple[int, int, int], str]: ...
def asksaveasfilename(
    *,
    confirmoverwrite: bool | None = True,
    defaultextension: str | None = "",
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> str: ...
def askopenfilename(
    *,
    defaultextension: str | None = "",
    filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = ...,
    initialdir: StrOrBytesPath | None = ...,
    initialfile: StrOrBytesPath | None = ...,
    parent: Misc | None = ...,
    title: str | None = ...,
    typevariable: StringVar | str | None = ...,
) -> str: ...
def askdirectory(
    *,
    initialdir: StrOrBytesPath | None = ...,
    mustexist: bool | None = False,
    parent: Misc | None = ...,
    title: str | None = ...,
) -> str: ...
