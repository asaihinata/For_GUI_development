from datetime import datetime
from tkinter import Widget
from ...types import Any,ColorType,Literal,NoReturn,TupleInt2
from ..base import _Element
class Texts(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
class Buttons(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
class Input(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''Inputウィジェットに記入されている文字を取得する。

 :return: Inputウィジェットに記入されている文字を返す。
 :rtype: str'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def inserts(self,text:str='',place:int|Literal['end']='end')->NoReturn:'''挿入する位置を指定し,Inputウィジェットにその指定した場所のテキストを挿入する。

 :param text: 挿入する文字を指定する。
 :type text: str
 :param place: 文字を挿入する場所を指定する。
 :type place: int|Literal['end']'''
 def select_judge(self)->bool:'''Inputウィジェット内の文字が現在選択状態かを返す。

 :return: Inputウィジェット内の文字が現在選択状態かを返す。
 :rtype: bool'''
 def select_cansel(self)->NoReturn:'''Inputウィジェット内の選択状態を解除する。'''
 def all_delta(self)->NoReturn:'''Inputウィジェット内の文字を全て削除する。'''
class Multiline(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def inserts(self,text:str='',place:int|Literal['end']='end')->NoReturn:'''挿入する位置を指定し,Multilineウィジェットにその指定した場所のテキストを挿入する。

 :param text: 挿入する文字を指定する。
 :type text: str
 :param place: 文字を挿入する場所を指定する。
 :type place: int|Literal['end']'''
 def get_text(self)->str:'''Multilineウィジェットに記入されている文字を取得する。

 :return: Multilineウィジェットに記入されている文字を返す。
 :rtype: str'''
 def all_delta(self)->NoReturn:'''Multilineウィジェット内の文字を全て削除する。'''
class InputNumber(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def get_number(self)->int|float:'''InputNumberウィジェットに入力されている数値を取得する。

 :return: InputNumberウィジェットに入力されている数値を返す。
 :rtype: int|float'''
class Listboxs(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def select_set(self,val:int)->NoReturn:'''読み込み時にListboxsウィジェットで選択される項目を指定する。

 :param val: 読み込み時にListboxsウィジェットで選択される項目を指定する。
 :type val: int'''
 def apend(self,place:int|Literal['end']='end',lists:list=[])->NoReturn:'''Listboxsウィジェットに項目を追加する。

 :param lists: Listboxsウィジェットに追加する項目を指定する。
 :type lists: list
 :param place: 追加する場所を指定する。
 :type place: int|Literal['end']'''
 def clear(self)->NoReturn:'''Listboxsウィジェットの項目を全て削除する。'''
 def dele(self,*index:int)->NoReturn:'''Listboxsウィジェットの指定された箇所の項目を削除する。

 :param index: Listboxsウィジェットの削除したい項目の箇所を指定する。
 :type index: int'''
 def lens(self)->int:'''Listboxsウィジェットの項目数を取得する。

 :return: Listboxsウィジェットの項目数を取得する。
 :rtype: int'''
 def select(self)->tuple[int]:'''Listboxsウィジェットで選択された項目をタプルで返す。

 :return: Listboxsウィジェットで選択された項目を返す。
 :rtype: tuple[int]'''
 def select_val(self)->list[Any]|Any:'''Listboxsウィジェットで選択された項目の表記を返す。

 :return: Listboxsウィジェットで選択された項目の表記を返す。
 :rtype: list[Any]|Any'''
 def set(self,lists:tuple[str,...])->NoReturn:'''Listboxsウィジェットの項目をlitsに置き換える。

 :param lists: 新しく表示させたいListboxsウィジェットの項目を指定する。
 :type lists: tuple[str,...]'''
class Radio(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
class Checkbox(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def get_value(self)->bool:'''Checkboxウィジェットにチェックされているか判定する。未チェックの場合Falseを返す。

 :return: Checkboxウィジェットにチェックされているか判定する。
 :rtype: bool'''
 def set_value(self,value:bool)->NoReturn:'''Checkboxウィジェットのチェック状態を変更する。valueにbool型以外を指定した場合,Checkboxウィジェットのチェック状態の逆の状態を設置させる。

 :param value: チェック状態を指定する。チェック状態にする場合Trueを,未チェック状態にする場合Falseを指定する。
 :type value: bool'''
class Tree(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_iid(self)->list:'''Treeウィジェットの全てのiidを取得する。

 :return: Treeウィジェットの全てのiidを返す。
 :rtype: list'''
 def expand(self,iid:str)->NoReturn:'''指定した`iid`のツリーを開く。

 :param iid: 開きたい`iid`を指定する。
 :type iid: str'''
 def collapse(self,iid:str)->NoReturn:'''指定した`iid`のツリーを閉める。

 :param iid: ツリーを閉めたい`iid`を指定する。
 :type iid: str'''
 def get_path(self,iid:str)->str:'''指定した`iid`のサイド見出しを子孫を含め取得し,それらを結合し返す。

 :param iid: `iid`を指定する。
 :type iid: str
 :return: 指定した`iid`のサイド見出しを子孫を含め取得し,それらを結合し返す。
 :rtype: str'''
 def add_node(self,parent_iid:str,text:str,data_list:list)->str:'''指定した`iid`の子要素に新しいツリーを追加する。

 :param parent_iid: 追加先の`iid`を指定する。
 :type parent_iid: str
 :param text: `iid`のサイド見出しを指定する。
 :type text: str
 :param data_list: ツリーのコンテンツを指定する。
 :type data_list: list
 :return: 追加された`iid`名を返す。
 :rtype: str'''
 def delete_node(self,iid:str)->NoReturn:'''指定した`iid`を削除する。

 :param iid: 削除したい`iid`を指定する。
 :type iid: str'''
 def clear_width(self)->NoReturn:'''Treeウィジェットのセルの幅を均等に戻す。'''
class Table(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def clear_width(self)->NoReturn:'''Tableウィジェットのセルの幅を均等に戻す。'''
class Slidebar(_Element):
 def get(self)->int|float:'''Slidebarウィジェットの現在の値を取得する。

 :return: Slidebarウィジェットの現在の値を返す。
 :rtype: int|float'''
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def set(self,val:int|float)->NoReturn:'''Slidebarウィジェットの変更後の数値を設定する。

 :param val: 変更後の数値を指定する。
 :type val: int|float'''
class Menus(_Element):
 def get(self)->list:'''Menusウィジェットで表示されている配列を取得する。

 :return: Menusウィジェットで表示されている配列を返す。
 :rtype: list'''
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def clear(self)->NoReturn:'''Menusウィジェットのlistを空にしMenusウィジェットを非表示にする。'''
 def addmenu(self,label:str,submenu_lists:list)->NoReturn:'''Menusウィジェットに新しくメニューを追加する。

 :param label: メニューの表示文字を指定する。
 :type label: str
 :param submenu_lists: メニューに追加させるドロップダウンを指定する。
 :type submenu_lists: list'''
class Menubuttons(_Element):
 def get(self)->list:'''Menubuttonsウィジェットで表示されている配列を取得する。

 :return: Menusウィジェットで表示されている配列を返す。
 :rtype: list'''
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def clear(self)->NoReturn:'''Menubuttonsウィジェットのlistを空にしMenusウィジェットを非表示にする。'''
 def addmenu(self,label:str,submenu_lists:list)->NoReturn:'''Menubuttonsウィジェットに新しくメニューを追加する。

 :param label: メニューの表示文字を指定する。
 :type label: str
 :param submenu_lists: メニューに追加させるドロップダウンを指定する。
 :type submenu_lists: list'''
class Frames(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
class Column(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
class Tab(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def _add_tab(self,frame:Widget,title:str=...):'''Tabウィジェットに新しいタブを追加する。

 :param frame: 親ウィジェットを指定する。
 :type frame: Widget
 :param title: タイトルを指定する。
 :type title: str'''
class TCombobox(_Element):
 def get_text(self)->str:'''TComboboxウィジェットに記載されている文字を取得する。

 :return: TComboboxウィジェットに記載されている文字を返す。
 :rtype: str'''
 def set_text(self,text:str)->NoReturn:'''TComboboxウィジェットの文字を変更する。

 :param text: 文字を指定する。
 :type text: str'''
 def clear(self)->NoReturn:'''TComboboxウィジェットの文字を削除する。'''
class TProgressbar(_Element):
 def start(self)->NoReturn:'''TProgressbarをプログレスバーのバーを変化させる。'''
 def stop(self)->NoReturn:'''TProgressbarをプログレスバーのバーの変化を止める。'''
 def set(self,val:int|float)->NoReturn:'''TProgressbarウィジェットの値を指定する。

 :param val: TProgressbarウィジェットの値を指定する。
 :type val: int|float'''
 def get(self)->int|float:'''TProgressbarの値を取得する。

 :return: TProgressbarの値を返す。
 :rtype: int|float'''
class Link(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_link(self)->str:'''Linkウィジェットに登録されているURLを取得する。'''
 def set_link(self,link:str)->NoReturn:'''LinkウィジェットのURLを変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
class Images(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
class QRcode(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
class Barcode(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
class Calendars(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def move_date(self,year:int=None,month:int=None,day:int=None)->NoReturn:'''指定したyear,month,dayに移動する。

 :param year: 移動先の年を指定する。
 :type year: int
 :param month: 移動先の月を指定する。
 :type month: int
 :param day: 移動先の日にちを指定する。
 :type day: int'''
 def move_today(self)->NoReturn:'''本日の日付に移動する。'''
 def move_select(self)->NoReturn:'''Calendarsウィジェットで指定されている日付に移動する。'''
 def get_select(self)->datetime:'''Calendarsウィジェットで指定されている日付を取得する。'''
 def get_date(self)->str:'''Calendarsウィジェットで選択されている日にちを文字列で返す。

 :return: Calendarsウィジェットで選択されている日にちを文字列で返す。
 :rtype: str'''
 def select_clear(self)->NoReturn:'''Calendarsウィジェットに選択されている日付を消す。'''
 def nowdate_show(self)->TupleInt2:'''Calendarsウィジェットで表示されている年と月をタプルで(月,年)で返す。

 :return: Calendarsウィジェットで表示されている年と月をタプルで(月,年)で返す。
 :rtype: TupleInt2'''
class FolderLoad(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def dgettitle(self)->str:'''ダイアログに表示されるタイトルを取得する。

 :return: ダイアログのタイトルを返す。
 :rtype: str'''
 def dsettitle(self,titles:str)->NoReturn:'''ダイアログに表示されるタイトルを変更する。'''
 def get_path(self)->str:'''ファイルもしくはフォルダを選択し,選択されたパスを取得するダイアログを発生させるボタンを生成する。

 :return: ファイルもしくはフォルダのパスを返す。
 :rtype: str'''
class FileLoad(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def dgettitle(self)->str:'''ダイアログに表示されるタイトルを取得する。

 :return: ダイアログのタイトルを返す。
 :rtype: str'''
 def dsettitle(self,titles:str)->NoReturn:'''ダイアログに表示されるタイトルを変更する。'''
 def get_path(self)->str:'''ファイルもしくはフォルダを選択し,選択されたパスを取得するダイアログを発生させるボタンを生成する。

 :return: ファイルもしくはフォルダのパスを返す。
 :rtype: str'''
class Savebtn(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def dgettitle(self)->str:'''ダイアログに表示されるタイトルを取得する。

 :return: ダイアログのタイトルを返す。
 :rtype: str'''
 def dsettitle(self,titles:str)->NoReturn:'''ダイアログに表示されるタイトルを変更する。'''
 def get_path(self)->str:'''ファイルもしくはフォルダを選択し,選択されたパスを取得するダイアログを発生させるボタンを生成する。

 :return: ファイルもしくはフォルダのパスを返す。
 :rtype: str'''
class Colorbtn(_Element):
 def delta(self)->NoReturn:'''ウィジェットを削除する。'''
 def get_text(self)->str:'''ウィジェットが表示している文字を取得する。'''
 def set_text(self,txt:str)->NoReturn:'''ウィジェットが表示している文字を変更する。'''
 def get_fg(self)->ColorType:'''ウィジェットが表示している文字色を取得する。'''
 def set_fg(self,fg:ColorType)->NoReturn:'''ウィジェットが表示している文字色を変更する。'''
 def get_bg(self)->ColorType:'''ウィジェットが表示している背景色を取得する。'''
 def set_bg(self,bg:ColorType)->NoReturn:'''ウィジェットが表示している背景色を変更する。'''
 def dgettitle(self)->str:'''ダイアログに表示されるタイトルを取得する。

 :return: ダイアログのタイトルを返す。
 :rtype: str'''
 def dsettitle(self,titles:str)->NoReturn:'''ダイアログに表示されるタイトルを変更する。'''
 def get_color(self)->tuple[tuple[int,int,int],str]|tuple[None,None]:'''選択された色を取得する。

 :return: 選択された色のRGBと16進数カラーコードをタプルで((R,G,B),16進数カラーコード)で返す。
 :rtype: tuple[tuple[int,int,int],str]|tuple[NoReturn,NoReturn]'''