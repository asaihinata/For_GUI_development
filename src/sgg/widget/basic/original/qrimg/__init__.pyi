from tkinter import Label
from PIL.ImageTk import PhotoImage
from ....base import _Element
class QRImage(_Element):
 imgs:PhotoImage
 widget:Label
 def delta(self):'''ウィジェットを削除する。'''
 def show(self):'''QRコードを表示させる。'''