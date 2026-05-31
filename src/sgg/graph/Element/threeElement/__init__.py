from matplotlib.pyplot import rcParams
from mpl_toolkits.mplot3d.axes3d import Axes3D
from ....dev import allNones,bols,list2num,listchose,num0s,nums,parsecolor,range_num
from ...style import FontFile,Fontmanager,Fontname,Xlabel,Ylabel,Zlabel
from ..Graph import GElement
__all__=['threeElement']
class threeElement(GElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  # グラフの基盤
  self.elev=nums(kw.get('elev'),30)
  self.azim=nums(kw.get('azim'),45)
  self.ax:Axes3D=self.fig.add_subplot(111,projection='3d')
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
  self.zlabel=kw.get('zlabel')
  self.zlabelfg=allNones(kw.get('zlabelfg'),self.labelfg,self.fg)
  self.zlabelha=allNones(kw.get('zlabelha'),self.labelha)
  self.zlabelva=allNones(kw.get('zlabelva'),self.labelva)
  self.zlabelalpha=allNones(kw.get('zlabelalpha'),self.labelalpha,1)
  self.zlabelzorder=allNones(kw.get('zlabelzorder'),self.labelzorder,4)
  self.zlabelrotation=allNones(kw.get('zlabelrotation'),self.labelrotation,0)
  self.zlabelrotation_mode=allNones(kw.get('zlabelrotation_mode'),self.labelrotation_mode,True)
  self.zlabelfontname=allNones(kw.get('zlabelfontname'),self.labelfontname)
  self.zlabelfontpath=allNones(kw.get('zlabelfontpath'),self.labelfontpath)
  if self.zlabelfontname is None and self.zlabelfontpath is None:self.zlabelfont=self.labelfont
  elif self.zlabelfontname is None and self.zlabelfontpath is not None:self.zlabelfont=FontFile(self.zlabelfontpath)
  elif self.zlabelfontname is not None and self.zlabelfontpath is None:
   if self.zlabelfontname in Fontmanager.name():self.zlabelfont=Fontname(self.zlabelfontname)
   else:self.zlabelfont=self.labelfont
  elif self.zlabelfontname is not None and self.zlabelfontpath is not None:self.zlabelfont=FontFile(self.zlabelfontpath)
  else:self.zlabelfont=self.labelfont
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
  if isinstance(zticksrange,int|float):
   zticksrange=abs(zticksrange)
   negnum=zticksrange*-1
   self.zticksrange=(negnum,zticksrange)
  elif list2num(zticksrange):self.zticksrange=zticksrange
  else:self.zticksrange=(0,0)
  # その他
  if bols(kw.get('mouse_rotation')):self.ax.disable_mouse_rotation()
  self.ax.view_init(self.elev,self.azim)
  self._apply_theme_colors()
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
  self.set_title(self.title)
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
  if xlabel is not None:Xlabel(self.ax,xlabel,color=self.xlabelfg,ha=self.xlabelha,va=self.xlabelva,font=self.xlabelfont,rotation=self.xlabelrotation,rotation_mode=self.xlabelrotation_mode,alpha=self.xlabelalpha,zorder=self.xlabelzorder)
  if ylabel is not None:Ylabel(self.ax,ylabel,color=self.ylabelfg,ha=self.ylabelha,va=self.ylabelva,font=self.ylabelfont,rotation=self.ylabelrotation,rotation_mode=self.ylabelrotation_mode,alpha=self.ylabelalpha,zorder=self.ylabelzorder)
  if zlabel is not None:Zlabel(self.ax,zlabel,color=self.zlabelfg,ha=self.zlabelha,va=self.zlabelva,font=self.zlabelfont,rotation=self.zlabelrotation,rotation_mode=self.zlabelrotation_mode,alpha=self.zlabelalpha,zorder=self.zlabelzorder)
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
 def set_xticks(self,ticks,labels=None,minor=False):
  return self.ax.set_xticks(ticks,labels=labels,minor=minor)
 def set_yticks(self,ticks,labels=None,minor=False):
  return self.ax.set_yticks(ticks,labels=labels,minor=minor)
 def set_zticks(self,ticks,labels=None,minor=False):
  return self.ax.set_zticks(ticks,labels=labels,minor=minor)