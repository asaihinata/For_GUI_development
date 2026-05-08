from tkinter import Misc
from ...typing import Literal
def askcolor(
color:str=None,
title:str=...
)->tuple[None,None]|tuple[tuple[int,int,int],str]:'''色を尋ねるダイアログを表示させる。

 :param color: ダイアログが最初に表示されるときに選択される色を指定する。
 :type color: str
 :param title: ダイアログのタイトルを指定する。
 :type title: str
 :return: 選択された色を返す。
 :rtype: tuple[None,None]|tuple[tuple[int,int,int],str]'''
def asksaveasfilename(
defaultextension:str='',
filetypes:list[tuple[str]]=...,
initialdir:str=...,
initialfile:str=...,
title:str=...
)->str:'''ファイルを尋ね,そのファイルのパスを取得するダイアログを表示させる。

 :param defaultextension: ファイル拡張子が省略された時に自動付与される拡張子を指定する。
 :type defaultextension: str
 :param filetypes: (ラベル,パターン)のタプルからなるシーケンスであり,'*' ワイルドカードを利用する。
 :type filetypes: list[tuple[str]]
 :param initialdir: 最初に表示するディレクトリを指定する。
 :type initialdir: str
 :param initialfile: ダイアログ表示時の初期ファイル名を指定する。
 :type initialfile: str
 :param title: ダイアログのタイトルを指定する。
 :type title: str
 :return: ファイルのパスを返す。
 :rtype: str'''
def askopenfilename(
defaultextension:str='',
filetypes:list[tuple[str]]=...,
initialdir:str=...,
initialfile:str=...,
title:str=...
)->str:'''ファイルを尋ね,そのファイルのパスを取得するダイアログを表示させる。

 :param defaultextension: ファイル拡張子が省略された時に自動付与される拡張子を指定する。
 :type defaultextension: str
 :param filetypes: (ラベル,パターン)のタプルからなるシーケンスであり,'*' ワイルドカードを利用する。
 :type filetypes: list[tuple[str]]
 :param initialdir: 最初に表示するディレクトリを指定する。
 :type initialdir: str
 :param initialfile: ダイアログ表示時の初期ファイル名を指定する。
 :type initialfile: str
 :param title: ダイアログのタイトルを指定する。
 :type title: str
 :return: ファイルのパスを返す。
 :rtype: str'''
def askdirectory(
initialdir:str=...,
mustexist:bool=False,
parent:Misc=...,
title:str=...
)->str:'''ディレクトリを尋ね,ファイル名を返す。

 :param initialdir: 最初に表示するディレクトリ名を指定する。
 :type initialdir: str
 :param mustexist: 選択が既存のディレクトリである必要があるかどうかを指定する。
 :type mustexist: bool
 :param parent: ダイアログをその上に表示するウィンドウを指定する。
 :type parent: Misc
 :param title: ウィンドウのタイトルを指定する。
 :type title: str
 :return: ファイル名を返す。
 :rtype: str'''
class popups:
 '''指定されたタイトルとメッセージを持つ情報メッセージボックスを作成して表示します。'''
 def __init__(
self,
title:str='Information',
message:str='Information message',
icon:Literal['info','error','warning','question']='info'
)->None:'''指定されたタイトルとメッセージを持つ情報メッセージボックスを作成して表示します。

 :param title: 情報メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param icon: 情報メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: 情報メッセージボックスに表示させるメッセージを指定する。
 :type message: str'''
 def __str__(self)->str:...
 def get_select(self)->str:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: str'''
class popupw:
 '''指定されたタイトルとメッセージを含む警告メッセージボックスを作成して表示します。'''
 def __init__(
self,
title:str='Warning',
message:str='Warning message',
icon:Literal['info','error','warning','question']='warning'
)->None:'''指定されたタイトルとメッセージを含む警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str'''
 def __str__(self)->str:...
 def get_select(self)->str:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: str'''
class popupwyn:
 '''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つ警告メッセージボックスを作成して表示します。'''
 def __init__(
self,
title:str='Warning',
message:str='Warning message',
icon:Literal['info','error','warning','question']='warning'
)->None:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つ警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str'''
 def __str__(self)->str:...
 def get_select(self)->str:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: str'''
class popupe:
 '''指定されたタイトルとメッセージを持つエラーメッセージボックスを作成して表示します。'''
 def __init__(
self,
title:str='Error',
message:str='Error message',
icon:Literal['info','error','warning','question']='error'
)->None:'''指定されたタイトルとメッセージを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str'''
 def __str__(self)->str:...
 def get_select(self)->str:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: str'''
class popupeyn:
 '''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つエラーメッセージボックスを作成して表示します。'''
 def __init__(
self,
title:str='Error',
message:str='Error message',
icon:Literal['info','error','warning','question']='error'
)->None:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str'''
 def __str__(self)->str:...
 def get_select(self)->str:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: str'''
class popupq:
 '''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。'''
 def __init__(
self,
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->None:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str'''
 def __str__(self)->str:...
 def get_select(self)->str:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: str'''
class popupoc:
 '''「OK」か「キャンセル」を選択させるダイアログを表示させる。'''
 def __init__(
self,
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->None:'''「OK」か「キャンセル」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str'''
 def __bool__(self)->bool:...
 def get_select(self)->bool:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
class popupyn:
 '''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す。'''
 def __init__(
self,
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->None:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str'''
 def __bool__(self)->bool:...
 def get_select(self)->bool:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
class popupync:
 '''「はい(Yes)」「いいえ(No)」「キャンセル(Cancel)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す,「キャンセル(Cancel)」もしくはダイアログを閉じた場合Noneを返す。'''
 def __init__(
self,
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->None:'''「はい(Yes)」「いいえ(No)」「キャンセル(Cancel)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す,「キャンセル(Cancel)」もしくはダイアログを閉じた場合Noneを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str'''
 def __bool__(self)->bool:...
 def get_select(self)->bool|None:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: bool|None'''
class popuptry:
 '''操作を再試行するかどうかを尋ねる「再試行」ボタンと「キャンセル」ボタンが設置されたダイアログを表示させる。回答が「再試行」の場合はTrueを,「キャンセル」の場合はFalseを返します。'''
 def __init__(
self,
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->None:'''操作を再試行するかどうかを尋ねる「再試行」ボタンと「キャンセル」ボタンが設置されたダイアログを表示させる。回答が「再試行」の場合はTrueを,「キャンセル」の場合はFalseを返します。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str'''
 def __bool__(self)->bool:...
 def get_select(self)->bool:'''ダイアログで選択された値を返します。

 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
def popup(
title:str='Information',
message:str='Information message',
icon:Literal['info','error','warning','question']='info'
)->str:'''指定されたタイトルとメッセージを持つ情報メッセージボックスを作成して表示します。

 :param title: 情報メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: 情報メッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: 情報メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
def popupwarning(
title:str='Warning',
message:str='Warning message',
icon:Literal['info','error','warning','question']='warning'
)->str:'''指定されたタイトルとメッセージを含む警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
def popupwarningyesno(
title:str='Warning',
message:str='Warning message',
icon:Literal['info','error','warning','question']='warning'
)->str:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つ警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
def popuperror(
title:str='Error',
message:str='Error message',
icon:Literal['info','error','warning','question']='error'
)->str:'''指定されたタイトルとメッセージを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
def popuperroryesno(
title:str='Error',
message:str='Error message',
icon:Literal['info','error','warning','question']='error'
)->str:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
def popupquestion(
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->str:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
def popupokcansel(
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->bool:'''「OK」か「キャンセル」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
def popupyesno(
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->bool:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
def popupyesnocansel(
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->bool|None:'''「はい(Yes)」「いいえ(No)」「キャンセル(Cancel)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す,「キャンセル(Cancel)」もしくはダイアログを閉じた場合Noneを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool|None'''
def popuptrys(
title:str='Question',
message:str='Question message',
icon:Literal['info','error','warning','question']='question'
)->bool:'''操作を再試行するかどうかを尋ねる「再試行」ボタンと「キャンセル」ボタンが設置されたダイアログを表示させる。回答が「再試行」の場合はTrueを,「キャンセル」の場合はFalseを返します。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','error','warning','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''