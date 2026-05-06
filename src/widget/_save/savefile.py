from os.path import splitext
from pathlib import Path

from .._dialog import asksaveasfilename

__all__=['autofile_save']
class autofile_save:
 def __init__(
self,
title:str='file save',
filetypes:list[tuple[str,str]]=[('All files','*.*')],
initialdir:str=None,
initialfile:str=None,
defaultextension:str='.txt'
)->None:
  '''ファイルを保存する際,保存するファイル名を尋ねるダイアログを表示し,保存先のフォルダパスを取得する。

 :param title: ダイアログのタイトルを指定する。
 :type title: str
 :param filetypes: 保存できるファイル形式の選択肢を指定する。
 :type filetypes: list[tuple[str]]
 :param initialdir: ダイアログを開く初期ディレクトリを指定する。
 :type initialdir: str
 :param initialfile: ファイル名フィールドの初期を指定する。
 :type initialfile: str
 :param defaultextension: 拡張子が設定されていない時のデフォルトを指定する。
 :type defaultextension: str'''
  if filetypes==None:filetypes=[('All files','*.*')]
  try:
   if not Path(initialdir).is_dir():initialdir=None
  except:initialdir=None
  get_path=asksaveasfilename(title=title,initialfile=initialfile,initialdir=initialdir,filetypes=filetypes,defaultextension=defaultextension)
  if isinstance(get_path,str):
   if splitext(get_path)[1]!=defaultextension:self.get_path=get_path+defaultextension
   else:self.get_path=get_path
  elif get_path=='':self.get_path=None
 def __fspath__(self):
  if self.get_path is None:
   raise FileNotFoundError('ファイルが存在しません')
  return self.get_path