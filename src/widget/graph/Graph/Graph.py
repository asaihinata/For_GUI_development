from os import getcwd
from re import findall
from cycler import cycler
from matplotlib.axes._axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import rcParams
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import array,ndarray
from ....types import Arraytype,Numbertype
from ..._function import bols,listchose,num0s,num1s,parsecolor,range_num
from ..._log import Logger
from ..._save import autofile_save
from ...developer import LIST
from ..support import Manylist,Marker,NSolid,Onelist,Solid
from .style import Xaxis,Yaxis,Zaxis
logger=Logger(name='Graph',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
graph_color=['#4477aa','#ee7733',"#111211",'#aa66cc','#77aadd','#ffa94d','#55aa55','#cc3311','#cc99ff','#ff8888','#444444','#888888','#332288','#88ccee','#44aa99','#117733','#999933','#ddcc77','#cc6677','#882255','#aa4499','#dddddd']
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
  self.title=kw.get('title')
  self.color=self._color_check(kw.get('color',graph_color))
  rcParams['axes.prop_cycle']=cycler(color=self.color)
  self.alpha=range_num(num0s(kw.get('alpha'),1),0,1,1)
  self.dpi=num1s(kw.get('dpi'),100)
  self.width,self.height=self._size(kw.get('size'))
  # グラフの表示
  self.fig=Figure(figsize=(self.width/self.dpi,self.height/self.dpi),dpi=self.dpi,facecolor=self.graph_bg)
  self.ax:Axes|Axes3D=None
  # ラベル
  self.labeljudge=True
  self.anchor=self._anchor(kw.get('labelanchor'))
  self.labelplace=self._getlabelplace(self.anchor,kw.get('labelplace'))
  self.labeltitle=kw.get('labeltitle')
  self.labelframe=bols(kw.get('labelframe'))
  self.labelshadow=bols(kw.get('labelshadow'),False)
  self.labelalpha=range_num(num0s(kw.get('labelalpha'),1),0,1,1)
  # 目盛り
  self.ticksshow=bols(kw.get('ticksshow'),False)
  self.tight_layout=bols(kw.get('tight_layout'))
 def photo(self,filename='Graph',ex='.png',dpi=100):
  try:self.fig.savefig(str(autofile_save(title='画像を保存する',defaultextension=listchose(ex,['.png','.eps','.jpg','.jpeg','.pdf','.pgf','.ps','.raw','.rgba','.svg','.svgz','.tif','.tiff','.webp']),initialfile=filename,initialdir=getcwd())),dpi=num1s(dpi,100))
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
  if isinstance(sizes,Arraytype)and len(list(sizes))==2:
   if(isinstance(i,(int,float))for i in sizes):return tuple(sizes)
   else:
    if not isinstance(sizes[0],Numbertype):sizes[0]=500
    if not isinstance(sizes[1],Numbertype):sizes[1]=400
    return sizes
  else:return(500,400)
 def markers(self,serch=None,num=None):return self._list_loop(list(Marker(serch)),num)
 def lines(self,serch=None,num=None):return self._list_loop(list(Solid(serch)),num)
 def nlines(self,serch=None,num=None):return self._list_loop(list(NSolid(serch)),num)
 def legend(self,ncols=1):
  if self.labeljudge:self.ax.legend(ncols=ncols,bbox_to_anchor=self.anchor,loc=self.labelplace,title=self.labeltitle,frameon=self.labelframe,shadow=self.labelshadow,framealpha=self.labelalpha)
 def _anchor(self,val,other=None):
  if(isinstance(val,(list,tuple)) and (len(val)==2 or len(val)==4) and all(isinstance(i,(int,float))for i in val)):return val
  return other
 def _getlabelplace(self,place,other='upper right'):
  labelplacelist=['upper right','upper left','lower left','lower right','right','center left','center right','lower center','upper center','center','best']
  if isinstance(place,int) and 0<=place<=10:return labelplacelist[int]
  elif place in labelplacelist:return place
  return listchose(other,labelplacelist)
 def pielabel(self,data,label=None):
  lls=label
  if isinstance(lls,(list,tuple)):
   ldt,lla=len(data),len(lls)
   if lla<ldt:
    for i in range(ldt-lla):lls.append(lla+i+1)
   elif ldt<lla:lls=lls[:ldt]
  else:self.labeljudge=False
  return(lls,label,type(label))
 def labels(self,label,nums=None):
  if not isinstance(nums,(int,float)):nums=self.max_depth
  if label==None:self.labeljudge=False
  if isinstance(label,str):lis=LIST(lists=[label])
  elif isinstance(label,(list,tuple)):lis=LIST(lists=label)
  else:lis=LIST(lists='')
  return(lis.get(nums),label)
 def _arr(self,val,j=True):
  if not isinstance(val,(list,tuple,LIST,ndarray)):
   raise TypeError('配列の型を指定してください')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,(list,tuple)):reval=array(val)
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
  if not isinstance(val,(list,tuple,ndarray,LIST)):
   raise TypeError('配列の型を指定してください')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,(list,tuple)):reval=array(val)
  elif isinstance(val,LIST):reval=array(list(val))
  if j==True:self.max_depth=max(self.max_depth,reval.shape[0])
  return reval
 def _color_check(self,color):
  relist=graph_color
  if isinstance(color,str):relist=[parsecolor(color,graph_color[0])]
  elif isinstance(color,(list,tuple)):
   set_arr,judge=[],False
   for i in color:
    c=parsecolor(i)
    if c is not None:
     judge=True
     set_arr.append(c)
    if judge:relist=set_arr
  return relist
 def _list_loop(self,lin,num):return LIST(lin).get(num)