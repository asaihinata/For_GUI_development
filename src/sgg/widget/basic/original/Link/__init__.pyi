from tkinter import Label
from ....base import _Element
from .....typing import ColorType
__all__=['Link']
class Link(_Element):
 widget:Label
 def delta(self):'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str):'''ウィジェットが表示している文字を変更する。'''
 def get_link(self)->str:'''Linkウィジェットに登録されているURLを取得する。'''
 def set_link(self,link:str):'''LinkウィジェットのURLを変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType):'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType):'''ウィジェットが表示している背景色を変更する。'''