from os import getcwd
from cycler import cycler
from matplotlib.axes._axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import rcParams
from matplotlib.ticker import LinearLocator,MaxNLocator
from mpl_toolkits.mplot3d.axes3d import Axes3D
from numpy import array,ndarray
from ...types import Arraytype,Numbertype
from .._function import bols,list2num,listchose,num0s,num1s,nums,parsecolor,range_num
from .._log import Logger
from .._save import autofile_save
from ..developer import LIST,Number
from .support import Manylist,Marker,NSolid,Onelist,Solid
__all__=['twoDElement','threeDElement']
logger=Logger(name='Graph',format={'filename':None,'lineno':{'after':'行目'},'message':None}).get_logger()
graph_color=['#4477aa','#ee7733','#228833','#aa66cc','#77aadd','#ffa94d','#55aa55','#cc3311','#cc99ff','#ff8888','#444444','#888888','#332288','#88ccee','#44aa99','#117733','#999933','#ddcc77','#cc6677','#882255','#aa4499','#dddddd']
rcParams['font.family']='Meiryo'
rcParams['axes.prop_cycle']=cycler(color=graph_color)
class GElement:
 def __init__(self,master,kw):
  self.master,self.widget,self.graph,self.graphdata,self._canvas_widget,self.max_depth=master,None,True,[],None,1
  # グラフの基盤
  self.fg=parsecolor(kw.get('fg'),'#000000')
  self.graph_bg=parsecolor(kw.get('bg'),'#ffffff')
  self.graph_grid=parsecolor(kw.get('graph_grid'),'#b7b7b7')
  self.title=kw.get('title')
  color=self._color_check(kw.get('color',graph_color))
  rcParams['axes.prop_cycle']=cycler(color=color)
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
 def _pack(self):
  self._canvas_widget=FigureCanvasTkAgg(self.fig,master=self.master).get_tk_widget()
  self._canvas_widget.pack(side='left',padx=5,pady=5)
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
 def legend(self):
  if self.labeljudge:self.ax.legend(bbox_to_anchor=self.anchor,loc=self.labelplace,title=self.labeltitle,frameon=self.labelframe,shadow=self.labelshadow,framealpha=self.labelalpha)
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
  if not isinstance(val,(list,tuple,ndarray)):
   raise TypeError('配列の型を指定してください')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,(list,tuple)):reval=array(val)
  if len(reval.shape)==1:reval=array([reval])
  if j==True:self.max_depth=max(self.max_depth,reval.shape[0])
  return reval
 def _manyarr(self,val,j=True):
  val=self._arr(list(Manylist(val)),j)
  if len(val.shape)==2:return self._arr(val)
  return self._arr([val])
 def _onearr(self,val,j=True):return self._arr(list(Onelist(val)),j)
 def _dataarr(self,val,j=True):
  if not isinstance(val,(list,tuple,ndarray)):
   raise TypeError('配列の型を指定してください')
  if isinstance(val,ndarray):reval=val
  elif isinstance(val,(list,tuple)):reval=array(val)
  if j==True:self.max_depth=max(self.max_depth,reval.shape[0])
  return reval
 def _color_check(self,color):
  relist=graph_color
  if isinstance(color,str):relist=[parsecolor(color,graph_color[0])]
  elif isinstance(color,(list,tuple)):
   set_arr,judge=[],False
   for i in color:
    c=parsecolor(i)
    if c!=None:
     judge=True
     set_arr.append(c)
    if judge:relist=set_arr
  return relist
 def _list_loop(self,lin,num):return LIST(lin).get(num)
class twoDElement(GElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  # ラベル
  self.xlabel=kw.get('xlabel')
  self.ylabel=kw.get('ylabel')
  self.y_verwrit=listchose(kw.get('y_verwrit'),['vertical','horizontal'])
  # グリッド線
  self.grid_xy=bols(kw.get('grid_xy'))
  self.grid_x=bols(kw.get('grid_x'),False)
  self.grid_y=bols(kw.get('grid_y'),False)
  self.xmajorint=bols(kw.get('xmajorint'))
  self.ymajorint=bols(kw.get('ymajorint'))
  # グラフの基盤
  self.ax:Axes=self.fig.add_subplot(111)
  # 目盛り
  self.xticksshow=bols(kw.get('xticksshow'),False)
  self.yticksshow=bols(kw.get('yticksshow'),False)
  self.xticksdirection=listchose(kw.get('xticksdirection'),['out','in','inout'])
  self.yticksdirection=listchose(kw.get('yticksdirection'),['out','in','inout'])
  xticksrange=kw.get('xticksrange',0)
  yticksrange=kw.get('yticksrange',0)
  if isinstance(xticksrange,(int,float)):
   xticksrange=abs(xticksrange)
   negnum=xticksrange*-1
   self.xticksrange=(negnum,xticksrange)
  elif isinstance(xticksrange,Number):
   xticksrange=abs(xticksrange).value()
   negnum=xticksrange*-1
   self.xticksrange=(negnum,xticksrange,negnum,xticksrange)
  elif list2num(xticksrange):self.xticksrange=xticksrange
  else:self.xticksrange=(0,0)
  if isinstance(yticksrange,(int,float)):
   yticksrange=abs(yticksrange)
   negnum=yticksrange*-1
   self.yticksrange=(negnum,yticksrange)
  elif isinstance(yticksrange,Number):
   yticksrange=abs(yticksrange).value()
   negnum=yticksrange*-1
   self.yticksrange=(negnum,yticksrange,negnum,yticksrange)
  elif list2num(yticksrange):self.yticksrange=yticksrange
  else:self.yticksrange=(0,0)
  # その他
  self.x:ndarray
  self.y:ndarray
  self.data:ndarray
  self.setxy=bols(kw.get('setxy'))
  self.xnumticks=num0s(kw.get('xnumticks'),None)
  self.ynumticks=num0s(kw.get('ynumticks'),None)
  self.ax.xaxis.set_major_locator(MaxNLocator(integer=self.xmajorint))
  self.ax.xaxis.set_major_locator(LinearLocator(numticks=self.xnumticks))
  self.ax.yaxis.set_major_locator(MaxNLocator(integer=self.ymajorint))
  self.ax.yaxis.set_major_locator(LinearLocator(numticks=self.ynumticks))
 def _apply_theme_colors(self):
  self.ax.set_facecolor(self.graph_bg)
  self.ax.tick_params(colors=self.fg)
  if self.title!=None:
   self.ax.set_title(self.title)
   self.ax.title.set_color(self.fg)
  self.ax.xaxis.label.set_color(self.fg)
  self.ax.yaxis.label.set_color(self.fg)
  if self.grid_xy:self.ax.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
  else:
   self.ax.grid(False)
   if self.grid_x:self.ax.xaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
   if self.grid_y:self.ax.yaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
 def _apply_labels(self,xlabel,ylabel):
  self.ax.set_xlabel(xlabel,color=self.fg)
  self.ax.set_ylabel(ylabel,color=self.fg,rotation=self.y_verwrit)
 def _arys(self,data):
  if any(isinstance(i,(list,tuple))for i in data):return array(data)
  elif isinstance(data,list):return array([data])
  elif isinstance(data,(tuple,LIST)):return array([list(data)])
  elif isinstance(data,ndarray):return data
  raise TypeError('dataには配列の型を指定してください')
 def _xys(self,x,y):
  x,y=self._arys(x),self._arys(y)
  if 2<=x.shape[0] and 2<=y.shape[0]:
   if self.setxy:x=x[0]
   else:y=y[0]
  return x,y
 def _updates(self,**kw):
  self.fg=parsecolor(kw.get('fg'),self.fg)
  self.graph_bg=parsecolor(kw.get('bg'),self.graph_bg)
  self.graph_grid=parsecolor(kw.get('graph_grid'),self.graph_grid)
  self.title=kw.get('title',self.title)
  self.xlabel=kw.get('xlabel',self.xlabel)
  self.ylabel=kw.get('ylabel',self.ylabel)
  self.alpha=range_num(num0s(kw.get('alpha'),self.alpha),0,1,self.alpha)
 def _ticks(self):
  if self.ticksshow:
   self.ax.set_xticks([])
   self.ax.set_yticks([])
  else:
   if self.xticksshow:self.ax.set_xticks([])
   if self.yticksshow:self.ax.set_yticks([])
  rcParams['xtick.direction']=self.xticksdirection
  rcParams['ytick.direction']=self.yticksdirection
 def _adjustment(self):
  xlimmins,xlimmaxs=self.xticksrange
  xlimmin,xlimmax=self.ax.get_xlim()
  ylimmins,ylimmaxs=self.yticksrange
  ylimmin,ylimmax=self.ax.get_ylim()
  self.ax.set_xlim(xlimmin+xlimmins,xlimmax+xlimmaxs)
  self.ax.set_ylim(ylimmin+ylimmins,ylimmax+ylimmaxs)
  if self.tight_layout:self.fig.tight_layout()
 def clear(self):
  self.graphdata=[]
  self.ax.clear()
  self._ticks()
  self._apply_theme_colors()
 def invert(self):
  self.invert_y()
  self.invert_x()
 def invert_x(self):self.ax.invert_xaxis()
 def invert_y(self):self.ax.invert_yaxis()
 def getbound(self):return(self.ax.get_xbound(),self.ax.get_ybound())
 def getxbound(self):return self.ax.get_xbound()
 def getybound(self):return self.ax.get_ybound()
 def getticks(self):return(self.ax.get_xticks(),self.ax.get_yticks())
 def getxticks(self):return self.ax.get_xticks()
 def getyticks(self):return self.ax.get_yticks()
class threeDElement(GElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  # グラフの基盤
  self.elev=nums(kw.get('elev'),30)
  self.azim=nums(kw.get('azim'),45)
  self.ax:Axes3D=self.fig.add_subplot(111,projection='3d')
  # ラベル
  self.xlabel=kw.get('xlabel')
  self.ylabel=kw.get('ylabel')
  self.zlabel=kw.get('zlabel')
  # グリッド線
  self.grid_xyz=bols(kw.get('grid_xyz'))
  self.grid_x=bols(kw.get('grid_x'),False)
  self.grid_y=bols(kw.get('grid_y'),False)
  self.grid_z=bols(kw.get('grid_z'),False)
  # 目盛り
  self.xmajorint=bols(kw.get('xmajorint'))
  self.ymajorint=bols(kw.get('ymajorint'))
  self.zmajorint=bols(kw.get('zmajorint'))
  self.xticksshow=bols(kw.get('xticksshow'),False)
  self.yticksshow=bols(kw.get('yticksshow'),False)
  self.zticksshow=bols(kw.get('zticksshow'),False)
  self.xticksdirection=listchose(kw.get('xticksdirection'),['out','in','inout'])
  self.yticksdirection=listchose(kw.get('yticksdirection'),['out','in','inout'])
  xticksrange=kw.get('xticksrange',0)
  yticksrange=kw.get('yticksrange',0)
  zticksrange=kw.get('zticksrange',0)
  if isinstance(xticksrange,(int,float)):
   xticksrange=abs(xticksrange)
   negnum=xticksrange*-1
   self.xticksrange=(negnum,xticksrange)
  elif isinstance(xticksrange,Number):
   xticksrange=abs(xticksrange).value()
   negnum=xticksrange*-1
   self.xticksrange=(negnum,xticksrange,negnum,xticksrange)
  elif list2num(xticksrange):self.xticksrange=xticksrange
  else:self.xticksrange=(0,0)
  if isinstance(yticksrange,(int,float)):
   yticksrange=abs(yticksrange)
   negnum=yticksrange*-1
   self.yticksrange=(negnum,yticksrange)
  elif isinstance(yticksrange,Number):
   yticksrange=abs(yticksrange).value()
   negnum=yticksrange*-1
   self.yticksrange=(negnum,yticksrange,negnum,yticksrange)
  elif list2num(yticksrange):self.yticksrange=yticksrange
  else:self.yticksrange=(0,0)
  if isinstance(zticksrange,(int,float)):
   zticksrange=abs(zticksrange)
   negnum=zticksrange*-1
   self.zticksrange=(negnum,zticksrange)
  elif isinstance(zticksrange,Number):
   zticksrange=abs(zticksrange).value()
   negnum=zticksrange*-1
   self.zticksrange=(negnum,zticksrange,negnum,zticksrange)
  elif list2num(zticksrange):self.zticksrange=zticksrange
  else:self.zticksrange=(0,0)
  # その他
  if bols(kw.get('mouse_rotation')):self.ax.disable_mouse_rotation()
  self.ax.view_init(self.elev,self.azim)
  self._apply_theme_colors()
  self.xnumticks=num0s(kw.get('xnumticks'),None)
  self.ynumticks=num0s(kw.get('ynumticks'),None)
  self.znumticks=num0s(kw.get('znumticks'),None)
  self.ax.xaxis.set_major_locator(LinearLocator(numticks=self.xnumticks))
  self.ax.yaxis.set_major_locator(LinearLocator(numticks=self.ynumticks))
  self.ax.zaxis.set_major_locator(LinearLocator(numticks=self.znumticks))
  self.ax.xaxis.set_major_locator(MaxNLocator(integer=self.xmajorint))
  self.ax.yaxis.set_major_locator(MaxNLocator(integer=self.ymajorint))
  self.ax.zaxis.set_major_locator(MaxNLocator(integer=self.zmajorint))
 def _updates(self,**kw):
  self.fg=parsecolor(kw.get('fg'),self.fg)
  self.graph_bg=parsecolor(kw.get('bg'),self.graph_bg)
  self.graph_grid=parsecolor(kw.get('graph_grid'),self.graph_grid)
  self.title=kw.get('title',self.title)
  self.elev=nums(kw.get('elev'),self.elev)
  self.azim=nums(kw.get('azim'),self.azim)
  self.xlabel=kw.get('xlabel',self.xlabel)
  self.ylabel=kw.get('ylabel',self.ylabel)
  self.zlabel=kw.get('zlabel',self.zlabel)
  self.alpha=range_num(num0s(kw.get('alpha'),self.alpha),0,1,self.alpha)
 def _apply_theme_colors(self):
  self.ax.set_facecolor(self.graph_bg)
  self.ax.tick_params(colors=self.fg)
  self.ax.set_title(self.title)
  self.ax.title.set_color(self.fg)
  self.ax.xaxis.label.set_color(self.fg)
  self.ax.yaxis.label.set_color(self.fg)
  self.ax.zaxis.label.set_color(self.fg)
  self._apply_grid()
 def _apply_grid(self):
  if self.grid_xyz:self.ax.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
  else:
   if self.grid_x:self.ax.xaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
   if self.grid_y:self.ax.yaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
   if self.grid_z:self.ax.zaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
 def _apply_labels(self,xlabel,ylabel,zlabel):
  self.ax.set_xlabel(xlabel,color=self.fg)
  self.ax.set_ylabel(ylabel,color=self.fg)
  self.ax.set_zlabel(zlabel,color=self.fg)
  self._apply_grid()
 def _adjustment(self):
  xlimmins,xlimmaxs=self.xticksrange
  xlimmin,xlimmax=self.ax.get_xlim()
  ylimmins,ylimmaxs=self.yticksrange
  ylimmin,ylimmax=self.ax.get_ylim()
  zlimmins,zlimmaxs=self.zticksrange
  zlimmin,zlimmax=self.ax.get_zlim()
  self.ax.set_xlim(xlimmin+xlimmins,xlimmax+xlimmaxs)
  self.ax.set_ylim(ylimmin+ylimmins,ylimmax+ylimmaxs)
  self.ax.set_zlim(zlimmin+zlimmins,zlimmax+zlimmaxs)
  if self.tight_layout:self.fig.tight_layout()
 def clear(self):
  self.graphdata=[]
  self.ax.clear()
  self._ticks()
  self._apply_theme_colors()
 def _ticks(self):
  if self.ticksshow:
   self.ax.set_xticks([])
   self.ax.set_yticks([])
   self.ax.set_zticks([])
  else:
   if self.xticksshow:self.ax.set_xticks([])
   if self.yticksshow:self.ax.set_yticks([])
   if self.zticksshow:self.ax.set_zticks([])
  rcParams['xtick.direction']=self.xticksdirection
  rcParams['ytick.direction']=self.yticksdirection
 def invert(self):
  self.ax.invert_xaxis()
  self.ax.invert_yaxis()
  self.ax.invert_zaxis()
 def invert_x(self):self.ax.invert_xaxis()
 def invert_y(self):self.ax.invert_yaxis()
 def invert_z(self):self.ax.invert_zaxis()
 def getbound(self):return(self.ax.get_xbound(),self.ax.get_ybound(),self.ax.get_zbound())
 def getxbound(self):return self.ax.get_xbound()
 def getybound(self):return self.ax.get_ybound()
 def getzbound(self):return self.ax.get_zbound()
 def getticks(self):return(self.ax.get_xticks(),self.ax.get_yticks(),self.ax.get_zticks())
 def getxticks(self):return self.ax.get_xticks()
 def getyticks(self):return self.ax.get_yticks()
 def getzticks(self):return self.ax.get_zticks()