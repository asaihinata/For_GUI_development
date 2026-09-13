from tkinter.ttk import _Padding

from .element import Element

__all__ = ["TElement"]

class TElement(Element):
    style_list: list = []
    stylename: str = ...
    def _padding(self, *args) -> _Padding: ...
    def _unit_change(self, val) -> str | int | float: ...
