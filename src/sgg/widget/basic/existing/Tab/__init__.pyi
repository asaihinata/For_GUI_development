from tkinter.ttk import Notebook
from tkinter import Widget
from ....base import _Element
class Tab(_Element):
 widget:Notebook
 def delta(self):'''ウィジェットを削除する。'''
 def _add_tab(self,frame:Widget,title:str=...):'''Tabウィジェットに新しいタブを追加する。

 :param frame: 親ウィジェットを指定する。
 :type frame: Widget
 :param title: タイトルを指定する。
 :type title: str'''