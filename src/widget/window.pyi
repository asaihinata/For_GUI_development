from tkinter import Tk
from typing import Any,NoReturn,TypeAlias
from basic import *
from graph import *
AllWidget_Type:TypeAlias=Barcode|BarGraph|BarhGraph|Boxplot|Bubble|Buttons|Calendars|Checkbox|Colorbtn|Column|DScatter|Ecdf|Errorbar|Eventplot|FileLoad|FolderLoad|Frames|Funne|Hatplot|Hexbin|Hist|Images|Input|InputNumber|Linefill|LineGraph|Link|Listboxs|Menubuttons|Menus|Multiline|Pie|QRcode|Radio|Savebtn|Scatter|Slidebar|Stack|Stacked|Stackedh|Stem|Step|Tab|Table|TCombobox|Texts|TProgressbar|Tree|Violinplot|Waterfall|Waterfallh|Hist2d
class WindowController:
 __firstlineno__:int
 __module__:str
 __dict__:dict[str,Any]
 __doc__:str
 __sizeof__:int
 root:Tk
 @classmethod
 def __instancecheck__(cls,ins:Any)->bool:...
 def get(self,key:str)->AllWidget_Type:'''ウィジェットの情報を取得する。

 :param key: ウィジェットの情報を取得したい,そのウィジェットの指定されたkeyを指定する。
 :type key: str
 :rtype: AllWidget_Type'''
 def get_title(self)->str:'''ウィジェットのタイトルを取得する。'''
 def set_title(self,title:str)->NoReturn:'''ウィジェットのタイトルを設置する。'''
 def close(self)->NoReturn:'''windowウィジェットを終了させる。'''
 def maxwin(self)->NoReturn:'''ウィンドウを最大化させる。'''
 def minwin(self)->NoReturn:'''ウィンドウを最小化させる。'''
 def run(self)->NoReturn:'''windowのメインループを実行しウィンドウを表示させる。'''
 def scroll_to(self,key:str)->NoReturn:'''keyで指定したウィジェットのところに移動する。

 :param key: 移動先のウィジェットのkeyを指定する。
 :type key: str'''
 def widgetcount(self)->int:'''ウィンドウに表示されているウィジェットの数を返す。

 :return: ウィンドウに表示されているウィジェットの数を返す。
 :rtype: int'''
 def widgetdict(self)->dict[str,AllWidget_Type]:'''ウィジェットの'key'とウィジェットの辞書を返す。

 :return: ウィジェットのキー名とウィジェットの辞書を返す。
 :rtype: dict[str,AllWidget_Type]'''
 def widgetlist(self)->list[str]:'''表示されている全てのウィジェットの'key'名の配列を返す。

 :return: ウィジェットのキー名とウィジェットの辞書を返す。
 :rtype: list[str]'''
 def widgetall(self)->list[AllWidget_Type]:'''表示されている全てのウィジェットの配列を返す。

 :return: ウィジェットを返す。
 :rtype: list[AllWidget_Type]'''
 def tookphoto(self,file:str='window',ex:str='.png')->NoReturn:'''ウィンドウの画面をスクリーンショットをする。

 :param file: ファイル名を指定する。
 :type file: str
 :param ex: 画像の拡張名を指定する。
 :type ex: str'''
 def foreground(self,bools:bool=True)->NoReturn:'''ウィンドウを常に最前面にするか指定する。'''
 def fullscreen(self,bools:bool=True)->NoReturn:'''ウィンドウをフルスクリーンにする操作をする。'''
 def alpha(self,val:float=1.0)->NoReturn:'''ウィンドウの透明度を指定する。'''
 def deiconify(self)->NoReturn:'''ウィンドウを再び画面に表示させる。'''
 def withdraw(self)->NoReturn:'''ウィンドウを非表示にする。'''