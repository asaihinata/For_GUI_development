from pathlib import Path
from PIL.PngImagePlugin import PngImageFile
from .._dialog import asksaveasfilename
__all__=['autoimg_save']
file_dict=[('All files','*.*'),('avif file','*.avif'),('bmp file','*.bmp'),('blp file','*.blp'),('eps file','*.eps'),('gif file','*.gif'),('ico file','*.ico'),('im file','*.im'),('jpg file','*.jpg'),('jp2 file','*.jp2'),('png file','*.png'),('tif file','*.tif'),('webp file','*.webp'),('dib file','*.dib'),('jpeg file','*.jpeg'),('j2k file','*.j2k'),('tiff file','*.tiff')]
class autoimg_save:
 def __init__(
self,
data:PngImageFile=None,
title:str='image file save',
filetypes:list[tuple[str,str]]=[('All files','*.*'),('avif file','*.avif'),('bmp file','*.bmp'),('blp file','*.blp'),('eps file','*.eps'),('gif file','*.gif'),('ico file','*.ico'),('im file','*.im'),('jpg file','*.jpg'),('jp2 file','*.jp2'),('png file','*.png'),('tif file','*.tif'),('webp file','*.webp'),('dib file','*.dib'),('jpeg file','*.jpeg'),('j2k file','*.j2k'),('tiff file','*.tiff')],
initialdir:str=None,
initialfile:str=None,
defaultextension:str='.png'
)->None:
  '''ファイルを保存する際,保存するファイル名を尋ねるダイアログを表示し,保存先のフォルダパスを取得する。
 :param data: 画像データを指定する。
 :type data: Image
 :param title: ダイアログのタイトルを指定する。
 :type title: str
 :param filetypes:保存できるファイル形式の選択肢を指定する。
 :type filetypes: list[tuple[str]]
 :param initialdir: ダイアログを開く初期ディレクトリ。
 :type initialdir: str
 :param initialfile: ファイル名フィールドの初期を指定する。
 :type initialfile: str
 :param defaultextension: 拡張子が設定されていない時のデフォルトを指定する。
 :type defaultextension: str'''
  self.data=data
  if not isinstance(self.data,PngImageFile):
   raise TypeError('dataがPngImageFileの型ではありません')
  if not isinstance(filetypes,list)and not isinstance(filetypes[0],tuple|list):filetypes=file_dict
  try:
   if not Path(initialdir).is_dir():initialdir=None
  except:initialdir=None
  self.get_path=asksaveasfilename(title=title,initialfile=initialfile,initialdir=initialdir,filetypes=filetypes,defaultextension=defaultextension)
  if self.get_path=='':self.get_path=None
  else:self.data.save(self.get_path)
 def __fspath__(self):
  if self.get_path is None:
   raise FileNotFoundError('ファイルが存在しません')
  return self.get_path