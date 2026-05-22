from tkinter.ttk import Treeview
from ....base import _Element
class Table(_Element):
 widget:Treeview
 def delta(self):'''ウィジェットを削除する。'''
 def clear_width(self):'''Tableウィジェットのセルの幅を均等に戻す。'''