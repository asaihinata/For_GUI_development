from .graph import *
from .widget import *
from ._dialog import *
def counts():
 sgg.count+=1
 return sgg.count
class sgg:
 count=0
 @classmethod
 def window(cls,**kw):return WindowController(kw)
 @staticmethod
 def Menus(**kw):return{'count':counts(),'type':'Menus',**kw}
 @staticmethod
 def Menubuttons(**kw):return{'count':counts(),'type':'Menubuttons',**kw}
 @staticmethod
 def Texts(**kw):return{'count':counts(),'type':'Texts',**kw}
 @staticmethod
 def Link(**kw):return{'count':counts(),'type':'Link',**kw}
 @staticmethod
 def Images(**kw):return{'count':counts(),'type':'Images',**kw}
 @staticmethod
 def Imagebyte(**kw):return{'count':counts(),'type':'Imagebyte',**kw}
 @staticmethod
 def Imagelink(**kw):return{'count':counts(),'type':'Imagelink',**kw}
 @staticmethod
 def Buttons(**kw):return{'count':counts(),'type':'Buttons',**kw}
 @staticmethod
 def Input(**kw):return{'count':counts(),'type':'Input',**kw}
 @staticmethod
 def Multiline(**kw):return{'count':counts(),'type':'Multiline',**kw}
 @staticmethod
 def Table(**kw):return{'count':counts(),'type':'Table',**kw}
 @staticmethod
 def Tree(**kw):return{'count':counts(),'type':'Tree',**kw}
 @staticmethod
 def Listboxs(**kw):return{'count':counts(),'type':'Listboxs',**kw}
 @staticmethod
 def TCombobox(**kw):return{'count':counts(),'type':'TCombobox',**kw}
 @staticmethod
 def Radio(**kw):return{'count':counts(),'type':'Radio',**kw}
 @staticmethod
 def Checkbox(**kw):return{'count':counts(),'type':'Checkbox',**kw}
 @staticmethod
 def Frames(**kw):return{'count':counts(),'type':'Frames',**kw}
 @staticmethod
 def Column(**kw):return{'count':counts(),'type':'Column',**kw}
 @staticmethod
 def Slidebar(**kw):return{'count':counts(),'type':'Slidebar',**kw}
 @staticmethod
 def InputNumber(**kw):return{'count':counts(),'type':'InputNumber',**kw}
 @staticmethod
 def FileLoad(**kw):return{'count':counts(),'type':'FileLoad',**kw}
 @staticmethod
 def FolderLoad(**kw):return{'count':counts(),'type':'FolderLoad',**kw}
 @staticmethod
 def Colorbtn(**kw):return{'count':counts(),'type':'Colorbtn',**kw}
 @staticmethod
 def Savebtn(**kw):return{'count':counts(),'type':'Savebtn',**kw}
 @staticmethod
 def Tab(**kw):return{'count':counts(),'type':'Tab',**kw}
 @staticmethod
 def TProgressbar(**kw):return{'count':counts(),'type':'TProgressbar',**kw}
 @staticmethod
 def Barcode(**kw):return{'count':counts(),'type':'Barcode',**kw}
 @staticmethod
 def QRImage(**kw):return{'count':counts(),'type':'QRImage',**kw}
 @staticmethod
 def LineGraph(**kw):return{'count':counts(),'type':'LineGraph',**kw}
 @staticmethod
 def BarGraph(**kw):return{'count':counts(),'type':'BarGraph',**kw}
 @staticmethod
 def SSBarGraph(**kw):return{'count':counts(),'type':'SSBarGraph',**kw}
 @staticmethod
 def BarhGraph(**kw):return{'count':counts(),'type':'BarhGraph',**kw}
 @staticmethod
 def Funne(**kw):return{'count':counts(),'type':'Funne',**kw}
 @staticmethod
 def Pie(**kw):return{'count':counts(),'type':'Pie',**kw}
 @staticmethod
 def Boxplot(**kw):return{'count':counts(),'type':'Boxplot',**kw}
 @staticmethod
 def Waterfall(**kw):return{'count':counts(),'type':'Waterfall',**kw}
 @staticmethod
 def Waterfallh(**kw):return{'count':counts(),'type':'Waterfallh',**kw}
 @staticmethod
 def Scatter(**kw):return{'count':counts(),'type':'Scatter',**kw}
 @staticmethod
 def DScatter(**kw):return{'count':counts(),'type':'DScatter',**kw}
 @staticmethod
 def Stem(**kw):return{'count':counts(),'type':'Stem',**kw}
 @staticmethod
 def Step(**kw):return{'count':counts(),'type':'Step',**kw}
 @staticmethod
 def Stack(**kw):return{'count':counts(),'type':'Stack',**kw}
 @staticmethod
 def Hist(**kw):return{'count':counts(),'type':'Hist',**kw}
 @staticmethod
 def Linefill(**kw):return{'count':counts(),'type':'Linefill',**kw}
 @staticmethod
 def Ecdf(**kw):return{'count':counts(),'type':'Ecdf',**kw}
 @staticmethod
 def Errorbar(**kw):return{'count':counts(),'type':'Errorbar',**kw}
 @staticmethod
 def Eventplot(**kw):return{'count':counts(),'type':'Eventplot',**kw}
 @staticmethod
 def Hatplot(**kw):return{'count':counts(),'type':'Hatplot',**kw}
 @staticmethod
 def Hist2d(**kw):return{'count':counts(),'type':'Hist2d',**kw}
 @staticmethod
 def Violinplot(**kw):return{'count':counts(),'type':'Violinplot',**kw}
 @staticmethod
 def Hexbin(**kw):return{'count':counts(),'type':'Hexbin',**kw}
 @staticmethod
 def Stacked(**kw):return{'count':counts(),'type':'Stacked',**kw}
 @staticmethod
 def Stackedh(**kw):return{'count':counts(),'type':'Stackedh',**kw}
 @staticmethod
 def Barpolar(**kw):return{'count':counts(),'type':'Barpolar',**kw}
 @staticmethod
 def Stempolar(**kw):return{'count':counts(),'type':'Stempolar',**kw}
 @staticmethod
 def Errorpolar(**kw):return{'count':counts(),'type':'Errorpolar',**kw}
 @staticmethod
 def Linepolar(**kw):return{'count':counts(),'type':'Linepolar',**kw}
 @staticmethod
 def Eventpolar(**kw):return{'count':counts(),'type':'Eventpolar',**kw}
 @staticmethod
 def Scatterpolar(**kw):return{'count':counts(),'type':'Scatterpolar',**kw}
 @staticmethod
 def Violinpolar(**kw):return{'count':counts(),'type':'Violinpolar',**kw}
 @staticmethod
 def Radarplot(**kw):return{'count':counts(),'type':'Radarplot',**kw}
 @classmethod
 def Popup(cls,**kw):return popup(**kw)
 @classmethod
 def Popupwarning(cls,**kw):return popupwarning(**kw)
 @classmethod
 def Popupwarningyesno(cls,**kw):return popupwarningyesno(**kw)
 @classmethod
 def Popuperror(cls,**kw):return popuperror(**kw)
 @classmethod
 def Popuperroryesno(cls,**kw):return popuperroryesno(**kw)
 @classmethod
 def Popupquestion(cls,**kw):return popupquestion(**kw)
 @classmethod
 def Popupokcancel(cls,**kw):return popupokcansel(**kw)
 @classmethod
 def Popupyesno(cls,**kw):return popupyesno(**kw)
 @classmethod
 def Popupyesnocancel(cls,**kw):return popupyesnocansel(**kw)
 @classmethod
 def Popuptry(cls,**kw):return popuptrys(**kw)