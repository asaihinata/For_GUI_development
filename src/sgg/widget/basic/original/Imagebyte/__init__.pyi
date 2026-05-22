from io import BytesIO
from tkinter import Label
from PIL.ImageTk import PhotoImage
from ....base import _Element
from .....typing import *
class Imagebyte(_Element):
 byte:bytes|BytesIO
 imgs:PhotoImage
 widget:Label
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''