from datetime import datetime
from tkinter import StringVar,_Cursor
from typing import Union
from matplotlib.mlab import GaussianKDE
from numpy import ndarray
from numpy.typing import ArrayLike
from .types import *
from .widget import *
class sgg:
 @classmethod
 def window(
cls,
layout:list|tuple=...,
title:str='window',
load:function|tuple[function,...]|None=None,
bg:ColorType='#64778d',
scroll:bool=...,
scroll_x:bool=...,
scroll_y:bool=...,
size:TupleNumbertype2=(None,None),
maxmine:bool=False,
location:TupleNumbertype2=(0,0)
)->WindowController:'''ウィンドウを生成する。

 :param layout: ウィンドウで表示されるウィジェットを指定する。各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます。
 :type layout: list|tuple
 :param title: ウィンドウに表示されるタイトル名を指定する。
 :type title: str
 :param load: ウィンドウ表示時に実行される関数を指定する。
 :type load: function|tuple[function,...]|None
 :param bg: ウィンドウの背景を指定する。
 :type bg: ColorType
 :param scroll: ウィンドウのx軸,y軸方向にスクロールできるか指定する。
 :type scroll: bool
 :param scroll_x: ウィンドウのx軸方向にスクロールできるか指定する。
 :type scroll_x: bool
 :param scroll_y: ウィンドウのy軸方向にスクロールできるか指定する。
 :type scroll_y: bool
 :param size: ウィンドウの幅と高さを指定する。
 :type size: TupleNumbertype2
 :param maxmine: ウィンドウ表示時最大化するかを指定する。
 :type maxmine: bool
 :param location: ウィンドウの表示位置を指定する。
 :type location: TupleNumbertype2'''
 @staticmethod
 def Texts(
text:str=...,
size:TupleNumbertype2=(None,None),
bg:ColorType=...,
fg:ColorType=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
takefocus:bool=True,
key:str=...,
bd:Numbertype=0,
pady:Numbertype=...,
padx:Numbertype=...,
wraplength:Numbertype=0,
cursor:_Cursor=...,
justify:Literal['left','center','right']='left',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict[str,Any]:'''テキストを生成する。

 :param text: Textsウィジェットに表記させる文字を指定する。
 :type text: str'''
 @staticmethod
 def Link(
text:str=...,
link:Linktype|None=None,
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
wraplength:Numbertype=0,
cursor:_Cursor=...,
bd:Numbertype=0,
bg:ColorType=...,
fg:ColorType='#0000ee',
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=True,
overstrike:bool=False,
size:TupleNumbertype2=(None,None),
justify:Literal['left','center','right']='left',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict[str,Any]:'''リンクテキストを生成する。

 :param text: Linkウィジェットに表記させる文字を指定する。
 :type text: str
 :param link: Linkウィジェットが押されたときにブラウザで開くURLのリンクを指定する。
 :type link: Linktype|None'''
 @staticmethod
 def Images(
path:str=...,
byto:bytes=...,
size:TupleNumbertype2=(None,None),
name:str='No Images',
takefocus:bool=True,
key:str=...
)->dict[str,Any]:'''画像を生成する。

 :param path: Imagesウィジェットに表示させる画像のパスを指定する。
 :type path: str
 :param byto: Imagesウィジェットに表示させる画像のバイトデータを指定する。
 :type byto: bytos
 :param name: 指定されたpathもしくはbytoに何らかの例外が出た場合にImagesウィジェットに表示される文字を指定する。
 :type name: str
 :param size: 画像の大きさを指定する。
 :type size: TupleNumbertype2'''
 @staticmethod
 def Buttons(
text:str=...,
function:function|tuple[function,...]|None=...,
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
wraplength:Numbertype=0,
cursor:_Cursor=...,
bg:ColorType=...,
fg:ColorType=...,
bd:Numbertype=0,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
size:TupleNumbertype2=(None,None),
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w'
)->dict[str,Any]:'''ボタンを生成する。

 :param text: Buttonsウィジェットに表記させる文字を指定する。
 :type text: str
 :param function: Buttonsウィジェットが押された時実行される関数を指定する。
 :type function: function|tuple[function,...]|None'''
 @staticmethod
 def Input(
text:str=...,
show:str=...,
insertwidth:Numbertype=2,
insertbg:ColorType='#000000',
width:Numbertype=20,
key:str=...,
bd:Numbertype=0,
takefocus:bool=True,
cursor:_Cursor=...,
bg:ColorType=...,
fg:ColorType=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
justify:Literal['left','center','right']='left'
)->dict[str,Any]:'''入力欄を生成する。

 :param text: Inputウィジェットに表記させる文字を指定する。
 :type text: str
 :param width: Inputウィジェットの幅の長さを指定する。
 :type width: Numbertype
 :param insertwidth: Inputウィジェットの入力時の挿入ポイントの幅を指定する。
 :type insertwidth: Numbertype
 :param insertbg: Inputウィジェットの入力時の挿入ポイントの色を指定する。
 :type insertbg: ColorType
 :param show: 実際の入力内容の各文字の代わりに表示させる文字を指定する。
 :type show: str'''
 @staticmethod
 def Multiline(
text:str=...,
insertbg:ColorType='#000000',
insertwidth:Numbertype=2,
width:Numbertype=20,
height:Numbertype=5,
key:str=...,
bd:Numbertype=1,
takefocus:bool=True,
padx:Numbertype=...,
pady:Numbertype=...,
cursor:_Cursor=...,
bg:ColorType=...,
fg:ColorType=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
wrap:Literal['none','word','char']='none',
state:Literal['normal','disabled']='normal',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
justify:Literal['left','center','right']='left'
)->dict[str,Any]:'''テキストエリアを生成する。

 :param text: Multilineウィジェットに表記させる文字を指定する。
 :type text: str
 :param insertwidth: Multilineウィジェットの入力時の挿入ポイントの幅を指定する。
 :type insertwidth: Numbertype
 :param insertbg: Multilineウィジェットの入力時の挿入ポイントの色を指定する。
 :type insertbg: ColorType
 :param state: 選択操作の有無を指定する。normalは操作可能にする。disabledは操作不可能にする。
 :type state: Literal['normal','disabled']'''
 @staticmethod
 def Table(
header_fg:ColorType='#000000',
header_bg:ColorType='#cccccc',
values:list=...,
header:list=...,
height:Numbertype=1,
rowheader:list=...,
colwidth:Numbertype=120,
rowheight:Numbertype=50,
bg:ColorType='#e0e0e0',
key:str=...
)->dict[str,Any]:'''表を生成する。

 :param header_fg: Tableウィジェットの見出しの文字色を指定する。
 :type header_fg: ColorType
 :param header_bg: Tableウィジェットの見出しの背景色を指定する。
 :type header_bg: ColorType
 :param values: Tableウィジェット本体に表示させる文字の配列を指定する。
 :type values: list
 :param header: Tableウィジェット見出しに表示させる文字の配列を指定する。
 :type header: list
 :param rowheader: Tableウィジェットの縦列の見出しを配列で指定し,それを設置する。
 :type rowheader: list
 :param colwidth: Tableウィジェットの幅を指定する。
 :type colwidth: Numbertype
 :param rowheight: Tableウィジェットのセルの高さを指定する。
 :type rowheight: Numbertype
 :param height: Tableウィジェットに表示できる行を指定する。
 :type height: Numbertype'''
 @staticmethod
 def Tree(
values:list=...,
header:list=...,
key:str=...,
bg:ColorType='#e0e0e0',
colwidth:Numbertype=120,
header_fg:ColorType='#000000',
header_bg:ColorType='#cccccc',
rowheight:Numbertype=50,
side_header:str=...
)->dict[str,Any]:'''ツリーを生成する。

 :param header_fg: Treeウィジェットの見出しの文字色を指定する。
 :type header_fg: ColorType
 :param header_bg: Treeウィジェットの見出しの背景色を指定する。
 :type header_bg: ColorType
 :param side_header: Treeウィジェットの階層列のテキストを指定する。
 :type side_header: str
 :param values: Treeウィジェット本体に表示させる文字の配列を指定する。
 :type values: list
 :param header: Treeウィジェット見出しに表示させる文字の配列を指定する。
 :type header: list
 :param rowheader: Treeウィジェットの縦列の見出しを配列で指定し,それを設置する。
 :type rowheader: list
 :param colwidth: Treeウィジェットの幅を指定する。
 :type colwidth: Numbertype
 :param rowheight: Treeウィジェットのセルの高さを指定する。
 :type rowheight: Numbertype'''
 @staticmethod
 def Listboxs(
values:Arraytype=...,
width:Numbertype=20,
height:Numbertype=5,
selectfg:ColorType=...,
selectbg:ColorType=...,
select:int=0,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
fg:ColorType='#000000',
bg:ColorType='#e0e0e0',
bd:Numbertype=0,
state:Literal['normal','disabled']='normal',
exportselection:bool=False,
selectmode:Literal['browse','single','multiple','extended']='browse',
key:str=...
)->dict[str,Any]:'''リストボックスを生成する。

 :param values: Listboxウィジェットに表記させるリストを指定する。
 :type values: Arraytype
 :param selectfg: Listboxウィジェットのリストに選択されているリストの文字色を指定する。
 :type selectfg: ColorType
 :param selectbg: Listboxウィジェットのリストに選択されているリストの背景色を指定する。
 :type selectbg: ColorType
 :param select: 選択項目の初期値を指定する。
 :type select: int
 :param exportselection: 選択中の項目のコピー操作を指定する。
 :type exportselection: bool
 :param state: 選択操作の有無を指定する。normalは操作可能にする。disabledは操作不可能にする。
 :type state: Literal['normal','disabled']
 :param selectmode: 選択可能な項目数と操作方法を指定する。
 :type selectmode: Literal['browse','single','multiple','extended']'''
 @staticmethod
 def TCombobox(
values:list=[],
default:str=...,
state:Literal['normal','readonly','disabled']='normal',
key:str=...,
bd:Numbertype=0,
padx:Numbertype=...,
pady:Numbertype=...
)->dict[str,Any]:'''コンボボックスを生成する。

 :param values: 選択項目を指定する。
 :type values: list
 :param default: 入力項目の初期テキストを指定する。
 :type default: str
 :param state: 値の入力制限やTComboboxウィジェットの有効化や無効化について指定する。
 :type state: Literal['normal','readonly','disabled']'''
 @staticmethod
 def Radio(
text:str=...,
group:str='default',
key:str=...,
wraplength:Numbertype=0,
bd:Numbertype=0
)->dict[str,Any]:'''ラジオボタンを生成する。読み込み時,グループの最初のRadioウィジェットが選択される。

 :param text: Radioウィジェットに表記させる文字を指定する。
 :type text: str
 :param group: Radioウィジェットのグループを指定する。同じ名前にすることで,そのグループ内で排他的な選択を実施する。
 :type group: str'''
 @staticmethod
 def Checkbox(
text:str=...,
default:bool=False,
wraplength:Numbertype=0,
bd:Numbertype=0,
key:str=...
)->dict[str,Any]:'''チェックボタンを生成する。

 :param text: Checkboxウィジェットに表記させる文字を指定する。
 :type text: str
 :param default: 読み込み時,Checkboxウィジェットがチェックするかを指定する。
 :type default: bool'''
 @staticmethod
 def Frames(
title:str=...,
layout:list=...,
labelanchor:Literal['nw','n','ne','w','center','e','sw','s','se']='nw',
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
cursor:_Cursor=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
bg:ColorType=...,
fg:ColorType=...,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='solid',
bd:Numbertype=1
)->dict[str,Any]:'''枠線付きのフレームを生成する。

 :param layout: Framesウィジェットに表示させるウィジェットを指定する。各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます。
 :type layout: list[list]
 :param labelanchor: タイトルを表記する場所を指定する。
 :type labelanchor: Literal['nw','n','ne','w','center','e','sw','s','se']
 :param title: Framesウィジェットのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def Menus(
list:list=...,
tearoff:bool=False,
takefocus:bool=True,
cursor:_Cursor=...,
bg:ColorType=...,
fg:ColorType=...,
bd:Numbertype=0,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
key:str=...
)->dict[str,Any]:'''メニューバーを生成する。

 :param list: Menusウィジェットに表示させるメニューを指定する。
 :type list: list
 :param tearoff: メニューウィジェットを独立したウィンドウにするかを指定する。
 :type tearoff: bool'''
 @staticmethod
 def Menubuttons(
list:list=...,
text:str=...,
tearoff:bool=False,
key:str=...,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
cursor:_Cursor=...,
bg:ColorType=...,
fg:ColorType=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict[str,Any]:'''メニューボタンを生成する。

 :param text: MenuButtonsウィジェットのボタンに表記させる文字を指定する。
 :type text: str
 :param list: MenuButtonsウィジェットに表示させるメニューを指定する。
 :type list: list
 :param tearoff: メニューウィジェットを独立したウィンドウにするかを指定する。
 :type tearoff: bool'''
 @staticmethod
 def Column(
layout:list[list]=[[]],
key:str=...,
bd:Numbertype=0,
takefocus:bool=True,
pady:Numbertype=...,
padx:Numbertype=...,
cursor:_Cursor=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False,
bg:ColorType=...,
fg:ColorType=...,
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat'
)->dict[str,Any]:'''フレームを生成する。

 :param layout: Columnウィジェットに表示させるウィジェットを指定する。各リストがウィンドウのその行に対応し,その中に配置したウィジェットが左から順に並びます。
 :type layout: list[list]'''
 @staticmethod
 def Slidebar(
value:Numbertype=0,
digits:int=0,
resolution:Numbertype=1,
length:Numbertype=200,
orientation:Literal['horizontal','vertical']='horizontal',
min:Numbertype=0,
max:Numbertype=100,
key:str=...,
bd:Numbertype=1
)->dict[str,Any]:'''スライダーを生成する。

 :param digits: スケールの値を文字列として取得した際の数値の最大桁数を指定する。
 :type digits: int
 :param resolution: スライダーのステップ数を指定する。
 :type resolution: Numbertype
 :param length: Slidebarウィジェットの長さを指定する。
 :type length: Numbertype
 :param orientation: Slidebarウィジェットの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param min: Slidebarウィジェットの数値の最小値を指定する。
 :type min: Numbertype
 :param max: Slidebarウィジェットの数値の最大値を指定する。
 :type max: Numbertype
 :param value: Slidebarウィジェットの読み込み時の初期値を指定する。
 :type value: Numbertype'''
 @staticmethod
 def InputNumber(
values:Numbertype=0,
min:Numbertype=0,
max:Numbertype=100,
insertwidth:Numbertype=2,
insertbg:ColorType='#000000',
increment:Numbertype=1,
width:Numbertype=20,
wrap:bool=False,
key:str=...,
bg:ColorType=...,
bd:Numbertype=0,
justify:Literal['left','center','right']='left'
)->dict[str,Any]:'''数値専用の入力欄を生成する。

 :param wrap: 数値が`max`もしくは`min`で指定した範囲外を選択しようとした場合,`max`より大きい数値の場合は`min`へ`min`より小さい数値の場合は`max`へ移動するかを指定する。
 :type wrap: bool
 :param insertwidth: InputNumberウィジェットの入力時の挿入ポイントの幅を指定する。
 :type insertwidth: Numbertype
 :param insertbg: InputNumberウィジェットの入力時の挿入ポイントの色を指定する。
 :type insertbg: ColorType
 :param increment: スライダーのステップ数を指定する。
 :type increment: Numbertype
 :param min: Slidebarウィジェットの数値の最小値を指定する。
 :type min: Numbertype
 :param max: Slidebarウィジェットの数値の最大値を指定する。
 :type max: Numbertype
 :param value: Slidebarウィジェットの読み込み時の初期値を指定する。
 :type value: Numbertype'''
 @staticmethod
 def FileLoad(
text:str='select File',
title:str='select File',
key:str=...,
bg:ColorType=...,
fg:ColorType=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict[str,Any]:'''ファイルパスを取得するダイアログを発生させるボタンを生成する。

 :param text: FileLoadウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: ファイルを選択するダイアログのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def FolderLoad(
text:str='select Folder',
title:str='select Folder',
key:str=...,
bg:ColorType=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict[str,Any]:'''ファイルパスを取得するダイアログを発生させるボタンを生成する。

 :param text: FolderLoadウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: フォルダを選択するダイアログのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def Savebtn(
initialfile:str=...,
initialdir:str=...,
filetypes:list[tuple[str]]=[('All files','*.*')],
defaultextension:str='.txt',
text:str='Save file',
title:str='Save file',
key:str=...,
bg:ColorType=...,
fg:ColorType=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict[str,Any]:'''ファイルもしくはフォルダを選択し,選択されたパスを取得するダイアログを発生させるボタンを生成する。

 :param text: Savebtnウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: フォルダを選択するダイアログのタイトルを指定する。
 :type title: str
 :param filetypes: 保存できるファイル形式の選択肢を指定する。
 :type filetypes: list[tuple[str]]
 :param initialdir: ダイアログを開く初期ディレクトリを指定する。
 :type initialdir: str
 :param initialfile: ファイル名フィールドの初期値を指定する。
 :type initialfile: str
 :param defaultextension: 拡張子が設定されていない時のデフォルトを指定する。
 :type defaultextension: str'''
 @staticmethod
 def Colorbtn(
color:ColorType='#ffffff',
text:str='select color',
title:str='select color',
key:str=...,
bg:ColorType=...,
fg:ColorType=...,
wraplength:Numbertype=0,
bd:Numbertype=0,
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='center'
)->dict[str,Any]:'''色を選択し,選択された色を取得するダイアログを発生させるボタンを生成する。

 :param color: ダイアログで選択される色の初期値を選択する。
 :type color: ColorType
 :param text: Colorbtnウィジェットのボタンに表示させる文字を指定する。
 :type text: str
 :param title: 色を選択するダイアログのタイトルを指定する。
 :type title: str'''
 @staticmethod
 def Calendars(
date:datetime=...,
selectmode:Literal['none','day']='day',
headersbg:ColorType='gray70',
headersfg:ColorType='black',
othermonthbg:ColorType='gray93',
othermonthfg:ColorType='gray45',
weekendbg:ColorType='gray80',
weekendfg:ColorType='gray30',
locale:str='ja_JP',
firstweekday:Literal['monday','sunday']='sunday',
format:str|Literal['format0','format1','format2','format3']='format0',
showweek:bool=False,
key:str=...,
justify:Literal['left','center','right']='left',
relief:Literal['raised','sunken','flat','ridge','solid','groove']='flat',
anchor:Literal['nw','n','ne','w','center','e','sw','s','se']='w',
bd:Numbertype=2,
weekenddays:TupleInt2|ListInt2=None,
state:Literal['normal','disabled']='normal',
textvariable:StringVar|None=None,
maxdate:datetime|None=None,
mindate:datetime|None=None,
showotherdays:bool=True
)->dict[str,Any]:'''カレンダーを生成する。

 :param date: Calendarsウィジェットに表示する日付を指定する。
 :type date: datetime
 :param selectmode: ユーザーがマウスクリックで選択した日を変更できるかどうかを指定する。
 :type selectmode: Literal['none','day']
 :param headersbg: 曜日列の背景色を指定する。
 :type headersbg: ColorType
 :param headersfg: 曜日列の文字色を指定する。
 :type headersfg: ColorType
 :param othermonthbg: Calendarsウィジェットで表示しいる月の前月と翌月に属する通常の曜日の背景色を指定する。
 :type othermonthbg: ColorType
 :param othermonthfg: Calendarsウィジェットで表示しいる月の前月と翌月に属する通常の曜日の文字色を指定する。
 :type othermonthfg: ColorType
 :param weekendbg: 週末の背景色を指定する。
 :type weekendbg: ColorType
 :param weekendfg: 週末の文字色を指定する。
 :type weekendfg: ColorType
 :param locale: ロケールを指定する。
 :type locale: str
 :param firstweekday: 週の最初の曜日を指定する。
 :type firstweekday: Literal['monday','sunday']
 :param format: 日付フォーマットを指定する。
 :type format: str|Literal['format0','format1','format2','format3']
 :param showweek: 週番号を表示するか指定する。
 :type showweek: bool
 :param weekenddays: 週末として表示する曜日を指定する。
 :type weekenddays: TupleInt2|ListInt2
 :param maxdate: 最大許容日付を指定する。
 :type maxdate: datetime|None
 :param mindate: 最小許容日付を指定する。
 :type mindate: datetime|None
 :param showotherdays: 前月の日付と翌月以降の日付を表示するか指定する。
 :type showotherdays: bool'''
 @staticmethod
 def Tab(
tabs:list[list[str,list[list]]]=[],
key:str=...,
bg:ColorType=...,
fg:ColorType=...,
family:fontname=...,
font_size:Numbertype=14,
weight:Literal['normal','bold']='normal',
slant:Literal['roman','italic']='roman',
underline:bool=False,
overstrike:bool=False
)->dict[str,Any]:'''タブを生成する。

 :param tabs: Tabウィジェットに表示させるウィジェットを指定する。配列の最初の要素にタブ名を,次の要素にTabウィジェットに表示させる`layout`を指定する。
 :type tabs: list[list[str,list[list]]]'''
 @staticmethod
 def TProgressbar(
value:Numbertype=0,
max:Numbertype=100,
length:Numbertype=200,
mode:Literal['determinate','indeterminate']='determinate',
orient:Literal['horizontal','vertical']='horizontal',
key:str=...
)->dict[str,Any]:'''プログレスバーを生成する。

 :param length: TProgressbarウィジェットの長さを指定する。
 :type length: Numbertype
 :param orient: TProgressbarウィジェットの向きを指定する。
 :type orient: Literal['horizontal','vertical']
 :param mode: 決定的モード(determinate)か非決定的モード(indeterminate)かを指定する。
 :type mode: Literal['determinate','indeterminate']
 :param max: TProgressbarウィジェットの数値の最大値を指定する。
 :type max: Numbertype
 :param value: TProgressbarウィジェットの読み込み時の初期値を指定する。
 :type value: Numbertype'''
 @staticmethod
 def Barcode(
data:str=...,
data_type:Literal['EAN-8','EAN-13','JAN','Code39','Code128']='Code128',
name:str='No Barcode image',
key:str=...
)->dict[str,Any]:'''バーコードを生成する。

 :param data: バーコードで表示させる値を指定する。
 :type data: str
 :param data_type: バーコードの形式を指定する。
 :type data_type: Literal['EAN-8','EAN-13','JAN','Code39','Code128']
 :param name: 何らかの例外が起こりバーコードが表示されなかった場合に表示する文字を指定する。
 :type name: str'''
 @staticmethod
 def QRcode(
text:str=...,
name:str='No Qrcode image',
key:str=...
)->dict[str,Any]:'''QRコードを生成する。

 :param text: QRコードを読みっとった際に表示させる値を指定する。
 :type text: str
 :param name: QRコードを生成する際,何らかの例外が起こった場合に表示する文字を指定する。
 :type name: str'''
 @staticmethod
 def LineGraph(
x:n_array,
y:n_array,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
y_verwrit:Literal['vertical','horizontal']='vertical',
linewidth:Numbertype=2,
alpha:Numbertype=1,
markersize:Numbertype=10,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']=None,
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''折線グラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
 :param markersize: 折線グラフのマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param marker: 折線グラフのマーカーを指定する。
 :type marker: LiteralLiteral[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param linestyle: 折線グラフの線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',': ','none',None,' ','']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def BarGraph(
x:o_array,
y:n_array,
logs:bool=False,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
width:Numbertype=1,
align:Literal['center','edge']='center',
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''縦軸棒グラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param logs: y軸を対数スケールにするかを指定する。
 :type logs: bool
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
 :param width: 縦軸棒グラフのバー幅を指定する。
 :type width: Numbertype
 :param align: x軸の縦軸棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def BarhGraph(
x:o_array,
y:n_array,
logs:bool=False,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
alpha:Numbertype=1,
height:Numbertype=1,
align:Literal['center','edge']='center',
key:str=...
)->dict[str,Any]:'''横軸棒グラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param logs: x軸を対数スケールにするかを指定する。
 :type logs: bool
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
 :param height: 横軸棒グラフのバーの幅を指定する。
 :type height: Numbertype
 :param align: x軸の横軸棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Funne(
data:o_array,
xmajormaxbins:int=11,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
linewidth:Numbertype=2,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
alpha:Numbertype=1,
height:Numbertype=1,
align:Literal['center','edge']='center',
key:str=...
)->dict[str,Any]:'''じょうごグラフを生成する。

 :param data: `data`のデータを指定する。
 :type data: o_array
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。2n+1(nは正の整数)の整数を指定する。
 :type xmajormaxbins: int
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param linewidth: 折線グラフの線の幅を指定する。
 :type linewidth: Numbertype
 :param height: 棒グラフのバーの幅を指定する。
 :type height: Numbertype
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Stacked(
data:n_array,
dataname:o_array,
width:Numbertype=0.8,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=(0,1),
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='lower left',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''積み上げ縦棒グラフを生成する。

 :param data: `data`を指定する。
 :type data: n_array
 :param dataname: カテゴリ名を指定する。
 :type dataname: o_array
 :param width: 積み上げ縦棒グラフの幅のサイズを指定する。
 :type width: Numbertype
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Stackedh(
data:n_array,
dataname:o_array,
height:Numbertype=0.8,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=(0,1),
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='lower left',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''積み上げ横棒グラフを生成する。

 :param data: `data`を指定する。
 :type data: n_array
 :param dataname: カテゴリ名を指定する。
 :type dataname: o_array
 :param height: 積み上げ横棒グラフの高さのサイズを指定する。
 :type height: Numbertype
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Pie(
data:o_array,
label:labeltype=...,
startangle:Numbertype=0,
startangletype:bool=True,
shadow:bool=False,
counterclock:bool=False,
labeldistance:Numbertype=1.1,
explode:list[int,float,Number]|tuple[int,float,Number]|int|float|Number=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''円グラフを生成する。

 :param data: `data`のデータを指定する。
 :type data: o_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param startangle: 各要素の出力を開始する角度を指定する。
 :type startangle: Numbertype
 :param startangletype: 各要素の出力を開始する角度を度数法(True)か弧度法(False)かを指定する。
 :type startangletype: bool
 :param shadow: 円グラフに影を追加するか指定する。
 :type shadow: bool
 :param counterclock: 時計回りで出力するか指定する。
 :type counterclock: bool
 :param labeldistance: 中心からラベルの距離を指定する。
 :type labeldistance: Numbertype
 :param explode: 中心から各セグメントの離す距離を指定する。
 :type explode: list[int,float,Number]|tuple[int,float,Number]|int|float|Number
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype'''
 @staticmethod
 def Boxplot(
data:n_array,
label:labeltype=...,
legend:bool=True,
fill:bool=False,
notch:bool=False,
showfliers:bool=True,
orientation:Literal['vertical','horizontal']='vertical',
width:Numbertype=0.15,
whis:float|TupleFloat2=1.5,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''箱ひげ図を生成する。

 :param data: `data`のデータを指定する。
 :type data: n_array
 :param label: 箱ひげ図のデータ名を指定する。指定しなかった場合`box`+データの数になる。例)box0,box1
 :type label: labeltype
 :param legend: 凡例を表示させるか指定する。
 :type legend: bool
 :param fill: 箱内を塗りつぶすかを指定する。
 :type fill: bool
 :param notch: 箱の中央をくびれさすか指定する。
 :type notch: bool
 :param showfliers: 外れ値を表示させるか指定する。
 :type showfliers: bool
 :param orientation: 箱ひげ図の向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param whis: ヒゲの位置を指定する。
 :type whis: float|TupleFloat2
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Waterfall(
x:o_array,
y:o_array,
sums:bool=False,
sumstext:str='sum',
colorline:ColorType='#4477aa',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
ucolor:ColorType='#156082',
dcolor:ColorType='#e97132',
width:Numbertype=1,
key:str=...
)->dict[str,Any]:'''x軸向きにバーを設置された滝グラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param sums: 合計値を表示するかを指定する。
 :type sums: bool
 :param sumstext: 合計のラベルを指定する。
 :type sumstext: str
 :param colorline: バーとバーを繋げる線の色を指定する。
 :type colorline: ColorType
 :param linestyle: バーとバーを繋げる線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param ucolor: 上昇バーの色を指定する。
 :type ucolor: ColorType
 :param dcolor: 下降バーの色を指定する。
 :type dcolor: ColorType
 :param width: バーの幅を指定する。
 :type width: Numbertype
'''
 @staticmethod
 def Waterfallh(
x:o_array,
y:o_array,
sums:bool=False,
sumstext:str='sum',
colorline:ColorType='#4477aa',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
ucolor:ColorType='#156082',
dcolor:ColorType='#e97132',
height:Numbertype=1,
key:str=...
)->dict[str,Any]:'''y軸向きにバーを設置された滝グラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param sums: 合計値を表示するかを指定する。
 :type sums: bool
 :param sumstext: 合計のラベルを指定する。
 :type sumstext: str
 :param colorline: バーとバーを繋げる線の色を指定する。
 :type colorline: ColorType
 :param linestyle: バーとバーを繋げる線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param ucolor: 上昇バーの色を指定する。
 :type ucolor: ColorType
 :param dcolor: 下降バーの色を指定する。
 :type dcolor: ColorType
 :param height: バーの幅を指定する。
 :type height: Numbertype
'''
 @staticmethod
 def Scatter(
x:n_array,
y:n_array,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']='o',
markersize:Numbertype=10,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''散布図を生成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param marker: 散布図のマーカーを指定する。
 :type marker: LiteralLiteral[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def DScatter(
x:o_array,
y:o_array,
z:o_array,
xlabel:str=...,
ylabel:str=...,
zlabel:str=...,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']='o',
markersize:Numbertype=10,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xyz:bool=True,
grid_x:bool=False,
grid_y:bool=False,
grid_z:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
zmajorint:bool=True,
zmajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
zticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
znumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
mouse_rotation:bool=True,
elev:Numbertype=30,
azim:Numbertype=45,
key:str=...
)->dict[str,Any]:'''3Dの散布図を生成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param z: `z`のデータを指定する。
 :type z: o_array
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param zlabel: z軸のラベルを指定する。
 :type zlabel: str
 :param marker: 散布図のマーカーを指定する。
 :type marker: LiteralLiteral[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xyz: x軸,y軸,z軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`,`grid_z`より優先度が高い。
 :type grid_xyz: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_y: bool
 :param grid_z: z軸にグリッド線を表示させるか指定する。`grid_xyz`より優先度が低い。
 :type grid_z: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param zticksrange: z軸の目盛の範囲を変更する。
 :type zticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param zmajorint: z軸の目盛りを整数で自動調整させるか指定する。
 :type zmajorint: bool
 :param zmajormaxbins: z軸の目盛りの数の最大数を指定する。
 :type zmajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸,z軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param zticksshow: z軸のグリッド線と目盛り値について表示するかを指定する。
 :type zticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param znumticks: z軸の目盛りの数を指定する。
 :type znumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param mouse_rotation: 表示されているグラフをマウスで操作できるか指定する。
 :type mouse_rotation: bool
 :param elev: 仰角を度数表記で指定する。
 :type elev: Numbertype
 :param azim: 方位角を度数表記で指定する。
 :type azim: Numbertype'''
 @staticmethod
 def Stem(
x:NpArraytype=...,
y:NpArraytype=...,
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
orientation:Literal['vertical','horizontal']='vertical',
bottom:Numbertype=0,
marker:Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']=...,
line:Literal['-','--','-.','-.']=...,
color:Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''幹図を生成する。

 :param x: `x`のデータを指定する。
 :type x: NpArraytype
 :param y: `y`のデータを指定する。
 :type y: NpArraytype
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param orientation: 茎の向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param bottom: ベースラインの位置を指定する。
 :type bottom: Numbertype
 :param marker: 幹のマーカーの種類を指定する。
 :type marker: Literal['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']
 :param line: 幹の線の種類を指定する。
 :type line: Literal['-','--','-.','-.']
 :param color: 色を指定する。
 :type color: Literal['r','g','b','c','m','y','k','w']|list[Literal['r','g','b','c','m','y','k','w']]|tuple[Literal['r','g','b','c','m','y','k','w']]
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Step(
data:n_array,
range:int|float|TupleNumbertype2=...,
fill:bool=False,
baseline:Numbertype=0,
orientation:Literal['vertical','horizontal']='vertical',
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
y_verwrit:Literal['vertical','horizontal']='vertical',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
key:str=...
)->dict[str,Any]:'''階段グラフを生成する。

 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param data: `data`のデータを指定する。
 :type data: n_array
 :param range: 階段の端の座標を配列もしくは数値で指定する。
 :type range: int|float|ListNumbertype2|TupleNumbertype2
 :param baseline: 階段の下端の開始位置を指定する。
 :type baseline: Numbertype
 :param fill: 階段の下部から`baseline`の間を塗りつぶすかを指定する。
 :type fill: bool
 :param orientation: グラフの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']'''
 @staticmethod
 def Hatplot(
x:o_array,
data:o_array,
color:ColorType='#4477aa',
label:labeltype=...,
xlabel:str=...,
ylabel:str=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''ハットグラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param data: `data`のデータを指定する。
 :type data: o_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Hist(
data:o_array,
label:labeltype=...,
width:Numbertype=1,
min:Numbertype=...,
max:Numbertype=...,
decimalpoint:Numbertype=0,
orientation:Literal['vertical','horizontal']='vertical',
bottom:Numbertype=0,
bins:int|list|range|tuple|ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
y_verwrit:Literal['vertical','horizontal']='vertical',
xlabel:str=...,
ylabel:str=...,
key:str=...
)->dict[str,Any]:'''ヒストグラムを生成する。

 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param data: `data`のデータを指定する。
 :type data: o_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param width: ヒストグラムのバーのサイズを指定する。
 :type width: Numbertype
 :param orientation: ヒストグラムの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param bottom: ヒストグラムのバーの位置を指定する。
 :type bottom: Numbertype
 :param min: ヒストグラムで表示される最小値を指定する。
 :type min: Numbertype
 :param max: ヒストグラムで表示される最大値を指定する。
 :type max: Numbertype
 :param decimalpoint: ヒストグラムのbinの小数点を指定する。
 :type decimalpoint: Numbertype
 :param bins: `bins`を指定する。
 :type bins: int|list|range|tuple|np.ndarray|Literal['auto','fd','doane','scott','stone','rice','sturges','sqrt']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']'''
 @staticmethod
 def Stack(
x:n_array,
y:n_array,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
hatch:Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']=None,
baseline:Literal['zero','sym','wiggle','weighted_wiggle']='zero',
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''積み上げエリアチャートを生成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param hatch: 塗りつぶし領域内の模様を指定する。
 :type hatch: Literal[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--',r'-\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']
 :param baseline: 基準値の算出方法を指定する。
 :type baseline: Literal['zero','sym','wiggle','weighted_wiggle']
 :param align: x軸の棒グラフバーの配置を指定する。
 :type align: Literal['center','edge']
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Bubble(
x:n_array,
y:n_array,
data:n_array,
bubblesize:Numbertype=1,
marker:Literal[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']='o',
markersize:Numbertype=10,
linewidth:Numbertype=2,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=0.5,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''バブルグラフを生成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param data: バブルグラフのバブルの大きさを指定する。
 :type data: n_array
 :param bubblesize: バブルの大きさの倍率を指定する。
 :type bubblesize: Numbertype
 :param marker: バブルグラフのマーカーを指定する。
 :type marker: LiteralLiteral[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
 :param markersize: 散布図のマーカーの大きさを指定する。
 :type markersize: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Linefill(
x:o_array,
ymin:n_array=...,
ymax:n_array=...,
centerlinewidth:Numbertype=2,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''積上げ面グラフを作成する。

 :param x: 曲線を定義する節点のx座標を指定する。
 :type x: o_array
 :param ymin: 最初の曲線を定義する節点のy座標を指定する。
 :type ymin: n_array
 :param ymax: 2つ目の曲線を定義する節点のy座標を指定する。
 :type ymax: n_array
 :param centerlinewidth: 線の太さを指定する。
 :type centerlinewidth: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Ecdf(
data:n_array,
complementary:bool=False,
compress:bool=False,
orientation:Literal['vertical','horizontal']='vertical',
linestyle:Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']='-',
linewidth:Numbertype=1.5,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''経験的累積分布関数を作成する。

 :param data: 入力データを指定する。
 :type data: n_array
 :param complementary: 補累積分布を描画するか指定する。
 :type complementary: bool
 :param compress: 同一値のデータをまとめて最適化するかどうか指定する。
 :type compress: bool
 :param orientation: プロットの向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param linestyle: 線の種類を指定する。
 :type linestyle: Literal['solid','-','dashed','--','dash-dot','-.','dotted',':','none',None,' ','']
 :param linewidth: 線の太さを指定する。
 :type linewidth: Numbertype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Errorbar(
x:n_array,
y:n_array,
err:o_array=...,
xerr:o_array=...,
yerr:o_array=...,
xuplims:bool=False,
xlolims:bool=False,
yuplims:bool=False,
ylolims:bool=False,
barsabove:bool=False,
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':']='solid',
marker:Literal['.','s','o','p','v','*','^','D']=None,
linewidth:Numbertype=1.5,
capthick:Numbertype=10,
capsize:Numbertype=0,
errorevery:int|tuple[int,...]=1,
color:ColorType|tuple[ColorType,...]=...,
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''誤差範囲付きの線グラフもしくはマーカーグラフ,あるいはその両方のエラーグラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: n_array
 :param y: `y`のデータを指定する。
 :type y: n_array
 :param err: `x`と`y`のデータの誤差の配列を指定する。
 :type err: o_array
 :param xerr: `x`のデータの誤差の配列を指定する。
 :type xerr: o_array
 :param yerr: `y`のデータの誤差の配列を指定する。
 :type yerr: o_array
 :param xuplims: `x`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type xuplims: bool
 :param xlolims: `x`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type xlolims: bool
 :param yuplims: `y`の上向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type yuplims: bool
 :param ylolims: `y`の下向きの誤差が「限界値」であることを示す矢印の状態にするか指定する。
 :type ylolims: bool
 :param barsabove: 誤差範囲をグラフ記号の上に表示させるか指定する。
 :type barsabove: bool
 :param linestyle: データ点とデータ点を結ぶ線の種類を指定する。
 :type linestyle: Literal['dashdot','dashed','dotted','solid','-','--','-.',':']
 :param marker: データ点のマーカーの種類を指定する。
 :type marker: Literal['.','s','o','p','v','*','^','D']
 :param linewidth: データ点を結ぶ線の太さを指定する。
 :type linewidth: Numbertype
 :param capthick: キャップの厚みを指定する。
 :type capthick: Numbertype
 :param capsize: エラーバーの先端にあるキャップの長さを指定する。
 :type capsize: Numbertype
 :param errorevery: エラーバーを表示する頻度を指定する。
 :type errorevery: int|tuple[int,...]
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Eventplot(
data:o_array,
linewidth:Numbertype=1,
linelength:Numbertype=1,
linestyle:Literal['dashdot','dashed','dotted','solid','-','--','-.',':']='solid',
orientation:Literal['vertical','horizontal']='vertical',
xlabel:str=...,
ylabel:str=...,
label:labeltype=...,
color:ColorType|tuple[ColorType,...]=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''イベントグラフを作成する。

 :param data: `data`のデータを指定する。
 :type data: o_array
 :param linewidth: エラーバーの線の太さを指定する。
 :type linewidth: Numbertype
 :param linelength: 線の合計の高さを指定する。
 :type linelength: Numbertype
 :param linestyle: 線の種類を指定する。
 :type linestyle: Literal['dashdot','dashed','dotted','solid','-','--','-.',':']
 :param orientation: 向きを指定する。
 :type orientation: Literal['horizontal','vertical']
 :param label: ラベルを指定する。
 :type label: labeltype
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @staticmethod
 def Hist2d(
x:o_array,
y:o_array,
max:Numbertype=...,
min:Numbertype=...,
xmax:Numbertype=...,
xmin:Numbertype=...,
ymax:Numbertype=...,
ymin:Numbertype=...,
bins:int|TupleInt2|ArrayLike|tuple[ArrayLike,ArrayLike]=10,
density:bool=False,
label:labeltype=...,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
yticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
y_verwrit:Literal['vertical','horizontal']='vertical',
xlabel:str=...,
ylabel:str=...,
key:str=...
)->dict[str,Any]:'''2次元ヒストグラムを生成する。

 :param x: `x`のデータを一次元配列で指定する。
 :type x: o_array
 :param y: `y`のデータを一次元配列で指定する。
 :type y: o_array
 :param max,min: 表示させたいカウントの範囲を指定する。
 :type max,min: Numbertype
 :param xmax,xmin: x軸の`bins`の範囲を指定する。
 :type xmax,xmin: Numbertype
 :param ymax,ymin: y軸の`bins`の範囲を指定する。
 :type ymax,ymin: Numbertype
 :param bins: ビンの数を指定する。
 :type bins: int|tuple[int,int]|ArrayLike|tuple[ArrayLike,ArrayLike]
 :param density: ヒストグラムを正規化かするかを指定する。
 :type density: bool
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :raises TypeError: `x`もしくは`y`もしくはその両方が二次元配列以上の多次元配列の場合に発生させる。
 :raises TypeError: `x`と`y`の要素の数が同じではない時に発生させる。'''
 @classmethod
 def Violinplot(
self,
data:n_array,
x:o_array,
y:o_array,
orientation:Literal['vertical','horizontal']='vertical',
width:Numbertype=1,
alpha:Numbertype=1,
showextrema:bool=True,
showmeans:bool=False,
showmedians:bool=False,
points:Numbertype=100,
bw_method:Literal['scott','silverman']|float|Callable[[GaussianKDE],float]='scott',
side:Literal['both','low','high']='both',
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''バイオリングラフを作成する。

 :param data: 入力データを指定する。
 :type data: n_array
 :param x: `orientation`が`vertical`の時にx軸上にバイオリンが設置される配列を指定する。
 :type x: n_array
 :param y: `orientation`が`horizontal`の時にy軸上にバイオリンが設置される配列を指定する。
 :type y: n_array
 :param orientation: バイオリンが設置される軸の向きを指定する。
 :type orientation: Literal['vertical','horizontal']
 :param width: バイオリンの幅を指定する。
 :type width: Numbertype
 :param showextrema: 極値を線で示すか指定する。
 :type showextrema: bool
 :param showmeans: 平均値を線で示すかどうか指定する。
 :type showmeans: bool
 :param showmedians: 中央値を線で示すかどうか指定する。
 :type showmedians: bool
 :param points: 各ガウスカーネル密度推定値を評価する点の数を指定する。
 :type points: Numbertype
 :param bw_method: 推定器の帯域幅を計算するために使用されるメソッドを指定する。
 :type bw_method: Literal['scott','silverman']|float|Callable[[GaussianKDE],float]
 :param side: バイオリンの左右対称もしくは左右(上下)のみを描画するか指定する。
 :type side: Literal['both','low','high']
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @classmethod
 def Hexbin(
self,
x:o_array,
y:o_array,
c:o_array|None=None,
gridsize:int|tuple[int,int]=100,
extent:tuple[float,float,float,float]|None=None,
xscale:Literal['linear','log']='linear',
yscale:Literal['linear','log']='linear',
mincnt:int=1,
bins:Literal['log']|int|tuple[float,...]|None=None,
size:TupleNumbertype2=(500,400),
fg:ColorType='#000000',
bg:ColorType='#ffffff',
color:ColorType|tuple[ColorType,...]=...,
title:str=...,
dpi:Numbertype=100,
alpha:Numbertype=1,
graph_grid:ColorType='#b7b7b7',
grid_xy:bool=True,
grid_x:bool=False,
grid_y:bool=False,
y_verwrit:Literal['vertical','horizontal']='vertical',
tight_layout:bool=True,
xticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
yticksrange:int|float|Number|tuple[int|tuple|Number,...]=0,
xmajorint:bool=True,
xmajormaxbins:Numbertype|Number=10,
ymajorint:bool=True,
ymajormaxbins:Numbertype|Number=10,
ticksshow:bool=False,
xticksshow:bool=False,
xticksdirection:Literal['out','in','inout']='out',
yticksshow:bool=False,
yticksdirection:Literal['out','in','inout']='out',
xnumticks:Numbertype|None=None,
ynumticks:Numbertype|None=None,
labelanchor:ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None=...,
labelplace:Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']='upper right',
labeltitle:str=...,
labelframe:bool=True,
labelshadow:bool=False,
labelalpha:Numbertype=1,
key:str=...
)->dict[str,Any]:'''2次元六角形グラフを作成する。

 :param x: `x`のデータを指定する。
 :type x: o_array
 :param y: `y`のデータを指定する。
 :type y: o_array
 :param c: 各ポイントの値を指定する。
 :type c: o_array
 :param gridsize: `bins`の細かさを指定する。
 :type gridsize: int|tuple[int,int]
 :param extent: 各ポイントの値を指定する。
 :type extent: tuple[float,float,float,float]|None
 :param xscale,yscale: 軸のスケールを指定する。
 :type xscale,yscale: Literal['linear','log']
 :param mincnt: 描画する`bins`の最小カウント数を指定する。
 :type mincnt: int
 :param bins: ビンのカウント方法を指定する。
 :type bins: Literal['log']|int|tuple[float,...]|None
 :param xlabel: x軸のラベルを指定する。
 :type xlabel: str
 :param ylabel: y軸のラベルを指定する。
 :type ylabel: str
 :param label: ラベルを指定する。
 :type label: labeltype
 :param title: グラフのタイトルを指定する。
 :type title: str
 :param color: 色を指定する。
 :type color: ColorType|tuple[ColorType,...]
 :param size: 表示させるグラフの大きさを指定する。
 :type size: TupleNumbertype2
 :param fg: グラフ内の文字色を指定する。
 :type fg: ColorType
 :param bg: グラフ内の背景色を指定する。
 :type bg: ColorType
 :param dpi: 1インチあたりのドット数を指定する。
 :type dpi: Numbertype
 :param alpha: グラフの透明度を指定する。
 :type alpha: Numbertype
 :param graph_grid: グラフのグリッド線の色を指定する。
 :type graph_grid: ColorType
 :param grid_xy: x軸とy軸にグリッド線を表示させるか指定する。`grid_x`,`grid_y`より優先度が高い。
 :type grid_xy: bool
 :param grid_x: x軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_x: bool
 :param grid_y: y軸にグリッド線を表示させるか指定する。grid_xyより優先度が低い。
 :type grid_y: bool
 :param y_verwrit: y軸のラベルを縦書きか横書きかを指定する。
 :type y_verwrit: Literal['horizontal','vertical']
 :param tight_layout: グラフのラベルやタイトルの位置を自動調整するか指定する。
 :type tight_layout: bool
 :param xticksrange: x軸の目盛の範囲を変更する。
 :type xticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param yticksrange: y軸の目盛の範囲を変更する。
 :type yticksrange: int|float|Number|tuple[int|tuple|Number,...]
 :param xmajorint: x軸の目盛りを整数で自動調整させるか指定する。
 :type xmajorint: bool
 :param xmajormaxbins: x軸の目盛りの数の最大数を指定する。
 :type xmajormaxbins: Numbertype|Number
 :param ymajorint: y軸の目盛りを整数で自動調整させるか指定する。
 :type ymajorint: bool
 :param ymajormaxbins: y軸の目盛りの数の最大数を指定する。
 :type ymajormaxbins: Numbertype|Number
 :param ticksshow: x軸,y軸のグリッド線と目盛り値について表示するかを指定する。
 :type ticksshow: bool
 :param xticksshow: x軸のグリッド線と目盛り値について表示するかを指定する。
 :type xticksshow: bool
 :param yticksshow: y軸のグリッド線と目盛り値について表示するかを指定する。
 :type yticksshow: bool
 :param xticksdirection: x軸の目盛りの向きを指定する。
 :type xticksdirection: Literal['out','in','inout']
 :param yticksdirection: y軸の目盛りの向きを指定する。
 :type yticksdirection: Literal['out','in','inout']
 :param xnumticks: x軸の目盛りの数を指定する。
 :type xnumticks: Numbertype|None
 :param ynumticks: y軸の目盛りの数を指定する。
 :type ynumticks: Numbertype|None
 :param labelanchor: 凡例の位置を指定する。
 :type labelanchor: ListNumbertype2|ListNumbertype4|TupleNumbertype2|TupleFloat4|None
 :param labelplace: 凡例の位置の基準点を指定する。
 :type labelplace: Literal['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
 :param labeltitle: 凡例のタイトルを指定する。
 :type labeltitle: bool
 :param labelframe: 凡例の背景を含む外枠を表示するか指定する。
 :type labelframe: bool
 :param labelshadow: 凡例に影を付与するか指定する。
 :type labelshadow: bool
 :param labelalpha: 凡例の背景の透明度を指定する。
 :type labelalpha: Numbertype'''
 @classmethod
 def Popup(
cls,
title:str='Information',
message:str='Information message',
icon:Literal['info','warning','error','question']='info'
)->str:'''指定されたタイトルとメッセージを持つ情報メッセージボックスを作成して表示します。

 :param title: 情報メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param icon: 情報メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :param message: 情報メッセージボックスに表示させるメッセージを指定する。
 :type message: str'''
 @classmethod
 def Popupwarning(
cls,
title:str='Warning',
message:str='Warning message',
icon:Literal['info','warning','error','question']='warning'
)->str:'''指定されたタイトルとメッセージを含む警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
 @classmethod
 def Popupwarningyesno(
cls,
title:str='Warning',
message:str='Warning message',
icon:Literal['info','warning','error','question']='warning'
)->Union[str]:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つ警告メッセージボックスを作成して表示します。

 :param title: 警告メッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: 警告メッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: 警告メッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[str] ('yes','no')'''
 @classmethod
 def Popuperror(
cls,
title:str='Error',
message:str='Error message',
icon:Literal['info','warning','error','question']='error'
)->str:'''指定されたタイトルとメッセージを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: str'''
 @classmethod
 def Popuperroryesno(
cls,
title:str='Error',
message:str='Error message',
icon:Literal['info','warning','error','question']='error'
)->Union[str]:'''指定されたタイトルとメッセージを含む「はい」と「いいえ」のボタンを持つエラーメッセージボックスを作成して表示します。

 :param title: エラーメッセージボックスに表示させるタイトル名を指定する。
 :type title: str
 :param message: エラーメッセージボックスに表示させるメッセージを指定する。
 :type message: str
 :param icon: エラーメッセージボックスに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[str] ('yes','no')'''
 @classmethod
 def Popupquestion(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->Union[str]:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[str] ('yes','no')'''
 @classmethod
 def Popupokcancel(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->bool:'''「OK」か「キャンセル」を選択させるダイアログを表示させる。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
 @classmethod
 def Popupyesno(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->bool:'''「はい(Yes)」か「いいえ(No)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''
 @classmethod
 def Popupyesnocancel(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->Union[bool,None]:'''「はい(Yes)」「いいえ(No)」「キャンセル(Cancel)」を選択させるダイアログを表示させる。「はい」の場合はTrueを,「いいえ」の場合はFalseを返す,「キャンセル(Cancel)」もしくはダイアログを閉じた場合Noneを返す。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: Union[bool,None]'''
 @classmethod
 def Popuptry(
cls,
title:str='Question',
message:str='Question message',
icon:Literal['info','warning','error','question']='question'
)->bool:'''操作を再試行するかどうかを尋ねる「再試行」ボタンと「キャンセル」ボタンが設置されたダイアログを表示させる。回答が「再試行」の場合はTrueを,「キャンセル」の場合はFalseを返します。

 :param title: ダイアログに表示させるタイトル名を指定する。
 :type title: str
 :param message: ダイアログに表示させるメッセージを指定する。
 :type message: str
 :param icon: ダイアログに表示させるアイコンを指定する。
 :type icon: Literal['info','warning','error','question']
 :return: ダイアログで選択された値を返す。
 :rtype: bool'''