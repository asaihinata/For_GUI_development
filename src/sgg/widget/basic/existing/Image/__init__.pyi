from tkinter import Label

from ....base import _Element

__all__=['Images']
class Images(_Element):
 widget:Label
 def delta(self):'''ウィジェットを削除する。'''