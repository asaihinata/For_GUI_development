from matplotlib.axes._axes import Axes
from matplotlib.pyplot import rcParams
from numpy import array,ndarray
from ..._function import allNones,bols,list2num,listchose,num0s,parsecolor,range_num
from .Graph import GElement
from .style import FontFile,Fontmanager,Fontname,Title,Xlabel,Ylabel
__all__=['twoElement']
class twoElement(GElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  # ラベル
  self.xlabel=kw.get('xlabel')
  self.xlabelfg=allNones(kw.get('xlabelfg'),self.labelfg,self.fg)
  self.xlabelha=allNones(kw.get('xlabelha'),self.labelha)
  self.xlabelva=allNones(kw.get('xlabelva'),self.labelva)
  self.xlabelalpha=allNones(kw.get('xlabelalpha'),self.labelalpha,1)
  self.xlabelzorder=allNones(kw.get('xlabelzorder'),self.labelzorder,4)
  self.xlabelrotation=allNones(kw.get('xlabelrotation'),self.labelrotation,'horizontal')
  self.xlabelrotation_mode=allNones(kw.get('xlabelrotation_mode'),self.labelrotation_mode,True)
  self.xlabelfontname=allNones(kw.get('xlabelfontname'),self.labelfontname)
  self.xlabelfontpath=allNones(kw.get('xlabelfontpath'),self.labelfontpath)
  if self.xlabelfontname is None and self.xlabelfontpath is None:self.xlabelfont=self.labelfont
  elif self.xlabelfontname is None and self.xlabelfontpath is not None:self.xlabelfont=FontFile(self.xlabelfontpath).Properties
  elif self.xlabelfontname is not None and self.xlabelfontpath is None:
   if self.xlabelfontname in Fontmanager.name():self.xlabelfont=Fontname(self.xlabelfontname).Properties
   else:self.xlabelfont=self.labelfont
  elif self.xlabelfontname is not None and self.xlabelfontpath is not None:self.xlabelfont=FontFile(self.xlabelfontpath)
  else:self.xlabelfont=self.labelfont
  self.ylabel=kw.get('ylabel')
  self.ylabelfg=allNones(kw.get('ylabelfg'),self.labelfg,self.fg)
  self.ylabelha=allNones(kw.get('ylabelha'),self.labelha)
  self.ylabelva=allNones(kw.get('ylabelva'),self.labelva)
  self.ylabelalpha=allNones(kw.get('ylabelalpha'),self.labelalpha,1)
  self.ylabelzorder=allNones(kw.get('ylabelzorder'),self.labelzorder,4)
  self.ylabelrotation=allNones(kw.get('ylabelrotation'),self.labelrotation,'vertical')
  self.ylabelrotation_mode=allNones(kw.get('ylabelrotation_mode'),self.labelrotation_mode,True)
  self.ylabelfontname=allNones(kw.get('ylabelfontname'),self.labelfontname)
  self.ylabelfontpath=allNones(kw.get('ylabelfontpath'),self.labelfontpath)
  if self.ylabelfontname is None and self.ylabelfontpath is None:self.ylabelfont=self.labelfont
  elif self.ylabelfontname is None and self.ylabelfontpath is not None:self.ylabelfont=FontFile(self.ylabelfontpath)
  elif self.ylabelfontname is not None and self.ylabelfontpath is None:
   if self.ylabelfontname in Fontmanager.name():self.ylabelfont=Fontname(self.ylabelfontname)
   else:self.ylabelfont=self.labelfont
  elif self.ylabelfontname is not None and self.ylabelfontpath is not None:self.ylabelfont=FontFile(self.ylabelfontpath)
  else:self.ylabelfont=self.labelfont
  # グリッド線
  self.grid_xy=bols(kw.get('grid_xy'))
  self.grid_x=bols(kw.get('grid_x'),False)
  self.grid_y=bols(kw.get('grid_y'),False)
  # グラフの基盤
  self.ax:Axes=self.fig.add_subplot(111)
  # 目盛り
  self.xmajorint=bols(kw.get('xmajorint'))
  self.ymajorint=bols(kw.get('ymajorint'))
  self.xticksshow=bols(kw.get('xticksshow'),False)
  self.yticksshow=bols(kw.get('yticksshow'),False)
  self.xticksdirection=listchose(kw.get('xticksdirection'),['out','in','inout'])
  self.yticksdirection=listchose(kw.get('yticksdirection'),['out','in','inout'])
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
  # その他
  self.x:ndarray
  self.y:ndarray
  self.data:ndarray
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
 def _apply_labels(self,xlabel,ylabel):
  if xlabel is not None:Xlabel(self.ax,xlabel,color=self.xlabelfg,ha=self.xlabelha,va=self.xlabelva,font=self.xlabelfont,rotation=self.xlabelrotation,rotation_mode=self.xlabelrotation_mode,alpha=self.xlabelalpha,zorder=self.xlabelzorder)
  if ylabel is not None:Ylabel(self.ax,ylabel,color=self.ylabelfg,ha=self.ylabelha,va=self.ylabelva,font=self.ylabelfont,rotation=self.ylabelrotation,rotation_mode=self.ylabelrotation_mode,alpha=self.ylabelalpha,zorder=self.ylabelzorder)
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