from matplotlib.projections.polar import PolarAxes
from numpy import array,linspace,ndarray,pi
from ...._function import bols,list2num,num0s,parsecolor,range_num
from ..Graph import GElement
from ...dev.maths.angle import *
from ...style import Title
from ...typing import Type_Numberlike
__all__=['polarElement']
pi2=2*pi
class polarElement(GElement):
 Anglegraph=True
 def __init__(self,master,kw):
  super().__init__(master,kw)
  # グリッド線
  self.grid_xy=bols(kw.get('grid_xy'))
  self.grid_x=bols(kw.get('grid_x'),False)
  self.grid_y=bols(kw.get('grid_y'),False)
  # グラフの基盤
  self.ax:PolarAxes=self.fig.add_subplot(111,projection='polar')
  self.set_Angletype(bols(kw.get('anglegraph')))
  # 目盛り
  self.xticksshow=bols(kw.get('xticksshow'),False)
  self.yticksshow=bols(kw.get('yticksshow'),False)
  xticksrange=kw.get('xticksrange',0)
  yticksrange=kw.get('yticksrange',0)
  if isinstance(xticksrange,int|float):
   xticksrange=abs(xticksrange)
   self.xticksrange=(xticksrange*-1,xticksrange)
  elif list2num(xticksrange):self.xticksrange=xticksrange
  else:self.xticksrange=(0,0)
  if isinstance(yticksrange,int|float):
   yticksrange=abs(yticksrange)
   self.yticksrange=(yticksrange*-1,yticksrange)
  elif list2num(yticksrange):self.yticksrange=yticksrange
  else:self.yticksrange=(0,0)
 def _places(self,num):return linspace(0,2*pi,num,endpoint=False)
 def _xyd(self,x,y,d=None):
  if d is None:return self._dataarr(x),self._dataarr(y)
  else:
   data=self._dataarr(d)
   return self._places(data.size),data
 def _apply_theme_colors(self):
  self.ax.set_facecolor(self.graph_bg)
  self.ax.tick_params(colors=self.fg)
  if self.title is not None:Title(self.ax,self.title,color=self.titlefg,ha=self.titleha,va=self.titleva,rotation=self.titlerotation,rotation_mode=self.titlerotation_mode,font=self.titlefont,alpha=self.titlealpha,zorder=self.titlezorder)
  self.ax.xaxis.label.set_color(self.fg)
  self.ax.yaxis.label.set_color(self.fg)
  if self.grid_xy:self.ax.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6,which='both')
  else:
   self.ax.grid(False)
   if self.grid_x:self.ax.xaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
   if self.grid_y:self.ax.yaxis.grid(True,color=self.graph_grid,linestyle='--',alpha=0.6)
 def _arys(self,data):
  if any(isinstance(i,list|tuple)for i in data):return array(data)
  elif isinstance(data,list):return array([data])
  elif isinstance(data,tuple|list):return array([list(data)])
  elif isinstance(data,ndarray):return data
  raise TypeError('dataには配列の型を指定してください')
 def _updates(self,**kw):
  self.fg=parsecolor(kw.get('fg'),self.fg)
  self.graph_bg=parsecolor(kw.get('bg'),self.graph_bg)
  self.graph_grid=parsecolor(kw.get('graph_grid'),self.graph_grid)
  self.title=kw.get('title',self.title)
  self.alpha=range_num(num0s(kw.get('alpha'),self.alpha),0,1,self.alpha)
 def _ticks(self):
  if self.ticksshow:
   self.ax.set_xticks([])
   self.ax.set_yticks([])
  else:
   if self.xticksshow:self.ax.set_xticks([])
   if self.yticksshow:self.ax.set_yticks([])
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
 def set_Angletype(self,angle=True):
  if isinstance(angle,bool):self.Anglegraph=angle
  else:
   raise TypeError('angleにはbool型を指定してください')
 def get_Angletype(self):return self.Anglegraph
 def set_thetalim(self,start,end):
  def r(maxs,start,end):
   if not isinstance(start,Type_Numberlike):start=0
   if not isinstance(end,Type_Numberlike):end=maxs
   if end<start:start,end=end,start
   if not 0<=start<=maxs:start=0
   if not 0<=end<=maxs:end=maxs
   return start,end
  if self.Anglegraph:
   s,e=r(360,start,end)
   return self.ax.set_thetalim(thetamin=s,thetamax=e)
  else:
   s,e=r(pi2,start,end)
   return self.ax.set_thetalim(minval=s,maxval=e)