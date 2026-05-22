from tkinter import Label
from PIL.ImageTk import PhotoImage
from ....base import _Element
class Barcode(_Element):
 imgs:PhotoImage
 widget:Label
 def delta(self):'''ウィジェットを削除する。'''