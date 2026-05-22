from tkinter import Label
from PIL.ImageTk import PhotoImage
from ....base import _Element
class Imagelink(_Element):
 imgs:PhotoImage
 widget:Label
 def delta(self):'''ウィジェットを削除する。'''