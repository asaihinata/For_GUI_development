from os import fspath,getcwd
from re import findall
from cycler import cycler
from matplotlib.axes._axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import rcParams
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import array,ceil,ndarray,tile
from ..._function import bols,listchose,num0s,num1s,nums,parsecolor,range_num
from ..._log import Logger
from ..._save import autofile_save
from ...dev import LIST
from .lists import Manylist,Onelist
from .style import FontFile,Fontmanager,Fontname,Legends,Marker,Solid
__all__=['GElement']
logger=Logger(name='Graph',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
graph_color=['#4477aa','#ee7733','#111211','#aa66cc','#77aadd','#ffa94d','#55aa55','#cc3311','#cc99ff','#ff8888','#444444','#888888','#332288','#88ccee','#44aa99','#117733','#999933','#ddcc77','#cc6677','#882255','#aa4499','#dddddd']
rcParams['font.family']='Meiryo'
rcParams['axes.prop_cycle']=cycler(color=graph_color)
class GElement:
 def __init__(self,master,kw):
  self.master=master
  self.widget=None
  self.graph=True
  self.graphdata=[]
  self._canvas_widget=None
  self.max_depth=1
  # グラフの基盤
  self.fg=parsecolor(kw.get('fg'),'#000000')
  self.graph_bg=parsecolor(kw.get('bg'),'#ffffff')
  self.graph_grid=parsecolor(kw.get('graph_grid'),'#b7b7b7')
  self.color=self._color_check(kw.get('color',graph_color))
  rcParams['axes.prop_cycle']=cycler(color=self.color)
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,1)
  self.dpi=num1s(kw.get('dpi'),100)
  self.width,self.height=self._size(kw.get('size'))
  # グラフの表示
  self.fig=Figure(figsize=(self.width/self.dpi,self.height/self.dpi),dpi=self.dpi,facecolor=self.graph_bg)
  self.ax:Axes|Axes3D=None
  # 凡例
  self.legendjudge=True
  self.anchor=self._anchor(kw.get('legendanchor'))
  self.legendplace=self._getlegendplace(self.anchor,kw.get('legendplace'))
  self.legendtitle=kw.get('legendtitle')
  self.legendframe=bols(kw.get('legendframe'))
  self.legendshadow=bols(kw.get('legendshadow'),False)
  self.legendalpha=range_num(num0s(kw.get('legendalpha'),1),0,1,1)
  self.legendncols=num1s(kw.get('legendncols',1))
  # 軸ラベル
  self.labelalpha=range_num(num0s(kw.get('labelalpha'),1),0,1,1)
  labelfg=kw.get('labelfg')
  if labelfg is None:self.labelfg=self.fg
  else:self.labelfg=labelfg
  self.labelzorder=nums(kw.get('labelzorder'),4)
  self.labelha=kw.get('labelha')
  self.labelva=kw.get('labelva')
  self.labelrotation=kw.get('labelrotation')
  self.labelrotation_mode=kw.get('labelrotation_mode')
  self.labelfontname=kw.get('labelfontname',None)
  self.labelfontpath=kw.get('labelfontpath',None)
  fontfamily=Fontname(rcParams['font.family'][0])
  if self.labelfontname is None and self.labelfontpath is None:self.labelfont=fontfamily
  elif self.labelfontname is None and self.labelfontpath is not None:self.labelfont=FontFile(self.labelfontpath)
  elif self.labelfontname is not None and self.labelfontpath is None:
   if self.labelfontname in Fontmanager.name():self.labelfont=Fontname(self.labelfontname)
   else:self.labelfont=fontfamily
  elif self.labelfontname is not None and self.labelfontpath is not None:self.labelfont=FontFile(self.labelfontpath)
  else:self.labelfont=fontfamily
  self.labelfont=self.labelfont.Properties
  # 目盛り
  self.ticksshow=bols(kw.get('ticksshow'),False)
  self.tight_layout=bols(kw.get('tight_layout'))
  # タイトル
  self.title=kw.get('title')
  self.titlealpha=range_num(num0s(kw.get('titlealpha'),1),0,1,1)
  self.titlezorder=nums(kw.get('titlezorder'),4)
  titlefg=kw.get('titlefg')
  if titlefg is None:self.titlefg=self.fg
  else:self.titlefg=titlefg
  self.titleha=kw.get('titleha')
  self.titleva=kw.get('titleva')
  self.titlerotation=kw.get('titlerotation')
  self.titlerotation_mode=kw.get('titlerotation_mode')
  self.titlefontname=kw.get('titlefontname',None)
  self.titlefontpath=kw.get('titlefontpath',None)
  fontfamily=Fontname(rcParams['font.family'][0])
  if self.titlefontname is None and self.titlefontpath is None:self.titlefont=fontfamily
  elif self.titlefontname is None and self.titlefontpath is not None:self.titlefont=FontFile(self.titlefontpath)
  elif self.titlefontname is not None and self.titlefontpath is None:
   if self.titlefontname in Fontmanager.name():self.titlefont=Fontname(self.titlefontname)
   else:self.titlefont=fontfamily
  elif self.titlefontname is not None and self.titlefontpath is not None:self.titlefont=FontFile(self.titlefontpath)
  else:self.titlefont=fontfamily
  self.titlefont=self.titlefont.Properties
 def photo(self,filename='Graph',ex='.png',dpi=100):
  try:self.fig.savefig(fspath(autofile_save(title='画像を保存する',defaultextension=listchose(ex,['.png','.eps','.jpg','.jpeg','.pdf','.pgf','.ps','.raw','.rgba','.svg','.svgz','.tif','.tiff','.webp']),initialfile=filename,initialdir=getcwd())),dpi=num1s(dpi,100))
  except Exception as e:
   logger.error(f'error:{e}')
 def winsize(self):
  root=self.master
  return root.winfo_width(),root.winfo_height()
 def winwidth(self):return self.master.winfo_width()
 def winheight(self):return self.master.winfo_height()
 def winxy(self):
  root=self.master
  return root.winfo_x(),root.winfo_y()
 def winx(self):return self.master.winfo_x()
 def winy(self):return self.master.winfo_y()
 def geometry(self):return[float(i) for i in findall(r'\d+',self.master.winfo_geometry())]
 def rootxy(self):
  root=self.master
  return root.winfo_rootx(),root.winfo_rooty()
 def rootx(self):return self.master.winfo_rootx()
 def rooty(self):return self.master.winfo_rooty()
 def visual(self):return self.master.winfo_visual()
 def screen(self):return self.master.winfo_screen()
 def reqsize(self):
  root=self.master
  return root.winfo_reqwidth(),root.winfo_reqheight()
 def reqwidth(self):return self.master.winfo_reqwidth()
 def reqheight(self):return self.master.winfo_reqheight()
 def id(self):return self.master.winfo_id()
 def name(self):return self.master.winfo_name()
 def _pack(self):
  self._canvas_widget=FigureCanvasTkAgg(self.fig,master=self.master)
  self._canvas_widget.get_tk_widget().pack(side='left',padx=5,pady=5)
 def _redraw(self):
  if self._canvas_widget is not None:self._canvas_widget.draw()
 def _size(self,sizes=(500,400)):
  if isinstance(sizes,list|tuple)and len(list(sizes))==2:
   if(isinstance(i,int|float)for i in sizes):return tuple(sizes)
   else:
    if not isinstance(sizes[0],int|float):sizes[0]=500
    if not isinstance(sizes[1],int|float):sizes[1]=400
    return sizes
  else:return(500,400)
 def markers(self,serch=None,num=None):
  if serch is None:serch='None'
  return self._list_loop(Marker(serch).marker,num)
 def lines(self,serch=None,num=None):return self._list_loop(Solid(serch).solid,num)
 def legend(self):
  if self.legendjudge:self.legend_=Legends(self.ax,ncols=self.legendncols,bbox_to_anchor=self.anchor,loc=self.legendplace,title=self.legendtitle,frameon=self.legendframe,shadow=self.legendshadow,framealpha=self.legendalpha)
 def _anchor(self,val,other=None):
  if(isinstance(val,list|tuple) and (len(val)==2 or len(val)==4) and all(isinstance(i,int|float)for i in val)):return val
  return other
 def _getlegendplace(self,place,other='upper right'):
  labelplacelist=['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
  if isinstance(place,int) and 0<=place<=10:return labelplacelist[place]
  elif place in labelplacelist:return place
  return listchose(other,labelplacelist)
 def pielabel(self,data,label=None):
  lls=label
  if isinstance(lls,list|tuple):
   ldt,lla=len(data),len(lls)
   if lla<ldt:
    for i in range(ldt-lla):lls.append(lla+i+1)
   elif ldt<lla:lls=lls[:ldt]
  else:self.legendjudge=False
  return(lls,label,type(label))
 def labels(self,label,nums=None):
  if not isinstance(nums,int|float):nums=self.max_depth
  if label==None:self.legendjudge=False
  if isinstance(label,str):lis=LIST(lists=[label])
  elif isinstance(label,list|tuple):lis=LIST(lists=label)
  else:lis=LIST(lists='')
  return(lis.get(nums),label)
 def _arr(self,val,j=True):
  if not isinstance(val,list|tuple|LIST|ndarray):
   raise TypeError('配列の型を指定してください')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,list|tuple):reval=array(val)
  elif isinstance(val,LIST):reval=array(list(val))
  if len(reval.shape)==1:reval=array([reval])
  if j==True:self.max_depth=max(self.max_depth,reval.shape[0])
  return reval
 def _manyarr(self,val,j=True):
  val=self._arr(list(Manylist(val)),j)
  if len(val.shape)==2:return self._arr(val)
  return self._arr([val])
 def _onearr(self,val,j=True):return self._arr(list(Onelist(val)),j)
 def _dataarr(self,val,j=True):
  if not isinstance(val,list|tuple|ndarray|LIST):
   raise TypeError('配列の型を指定してください')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,list|tuple):reval=array(val)
  elif isinstance(val,LIST):reval=array(list(val))
  if j==True:self.max_depth=max(self.max_depth,reval.shape[0])
  return reval
 def _color_check(self,color):
  relist=graph_color
  if isinstance(color,str):relist=[parsecolor(color,graph_color[0])]
  elif isinstance(color,list|tuple):
   set_arr,judge=[],False
   for i in color:
    c=parsecolor(i)
    if c is not None:
     judge=True
     set_arr.append(c)
    if judge:relist=set_arr
  return relist
 def _list_loop(self,lin,num):
  if not isinstance(lin,ndarray|list|tuple):lin=array([lin])
  if not isinstance(num,int):num=0
  return tile(lin,int(ceil(num/len(lin))))[:num]